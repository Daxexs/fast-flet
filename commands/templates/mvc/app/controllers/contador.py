import flet as ft
from fast_flet import MyController, MyPageResize
from models.contador import Model


class ContadorC(MyController):
    def __init__(self, _self: object, on_resize: MyPageResize = None) -> None:
        super().__init__(_self, on_resize)
        self.call.model = Model()

    def min(self,e):
        x = self.x # The object of class view created in view, where the parameter of the controller class is passed
        # GET VALUES FROM THE MODEL AND SEND THEM TO THE VIEW
        valor = self.call.model.test_min(x)
        print('MIN - Return value of model:',valor)
        x.numero.text = str(int(x.numero.text) - 1)
        x.update()

    def max(self,e):
        valor = self.call.model.test_max(self.x)
        print('MAX - Return value of model:',valor)
        self.x.numero.text = str(int(self.x.numero.text) + 1)
        self.x.update()

    def test_key(self):
        print('key:',self.call.on_keyboard_event.test)