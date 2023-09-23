import os
from importlib.util import spec_from_file_location, module_from_spec

moduleList = {}
modList = {}
STRUCTURE = ["view", "control", "model"]
LISTDIR = ["views","controllers","models"]


def add_class(
    ruta: str,
    dir_name: str,
):
    for filename in os.listdir(f"{ruta}/{dir_name}"):
        _file = os.path.join(f"{ruta}/{dir_name}", filename)
        if os.path.isfile(_file):
            filename = filename.strip(".py")
            if filename != "__init__":                             
                value = spec_from_file_location(filename, _file)
                moduleList[filename] = value

def pages_view()->dict:
    find = False
    with os.scandir(".") as it:
        moduleList.clear()
        for entry in it:
            if entry.name == "app":
                find = True
                if entry.is_file():
                    ruta = os.path.dirname(os.path.abspath(entry.name))
                    entry = os.listdir(ruta)
                else:
                    ruta = entry.path
                    entry: list = os.listdir(ruta)
                
                views = LISTDIR[0]

                if views in entry:
                    entry.remove(views)
                    entry.insert(0, views)
                    add_class(ruta, views)
                    break
                else:
                    raise ("Create the 'views' folder'")
            
            elif entry.name == "views":
                find=True
                ruta = os.path.dirname(os.path.abspath(entry))
                views = LISTDIR[0]
                add_class(ruta, views)
                break
        
        assert find, "You must create your project in a folder called 'app'."


    return moduleList

def routing() -> dict:
    modList.clear()
    inf = pages_view()
    for value2 in inf.values():
        data: dict = module_from_spec(value2)
        value2.loader.exec_module(data)   
        try:
            view = data.View()
            route = view.call.route
            modList[route] = {}          
            modList[route]['view'] = view            
            modList[route]['clear'] = view.call.page_clear          
        except Exception as e:
            raise e  
    return modList