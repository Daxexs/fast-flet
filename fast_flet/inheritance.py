from flet import Page, View, MainAxisAlignment, CrossAxisAlignment, KeyboardEvent, FloatingActionButton, AppBar, ScrollMode, NavigationBar, OptionalNumber
from dataclasses import dataclass

class Mykeyboard:
    """
    -> Use ```call```` on_keyboard_event

    ```
    add_control('<controller method>') # Adds a controller configuration (controller method), which is executed with the 'on_keyboard_event' event.
    def key() # returns the value entered by keyboard.
    def shift() # returns the value entered by keyboard.
    def ctrl() # returns the value entered by keyboard.
    def alt() # returns the value entered by keyboard.
    def meta() # returns the value entered by keyboard.
    def test() #returns a message of all the values ​​entered by keyboard. (key, Shift, Control, Alt, Meta)
    ```
    """
    def __init__(self, call=None) -> None:
        self.__call: KeyboardEvent = call
        self.controls: list = []

    @property
    def call(self):
        return self.__call

    @call.setter
    def call(self, call):
        self.__call = call

    def add_control(self, control: object):
        self.controls.append(control)

    async def _run_controls_async(self):
        for value in self.controls:
            try:
                await value()
            except:
                pass

    def _run_controls(self):
        for value in self.controls:
            try:
                value()
            except:
                pass

    def key(self):
        return self.__call.key

    def shift(self):
        return self.__call.shift

    def ctrl(self):
        return self.__call.ctrl

    def alt(self):
        return self.__call.alt

    def meta(self):
        return self.__call.meta

    def test(self):
        e = self.__call
        print(
            f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}")


class MyPageResize:
    """
    -> ```controls``` -> stores <add_control>

    -> use of methods ```on_resize```

    ```
    add_control('<control>', '<height>', '<max_height>') # Add a control that will be a response when executing the 'on_resize' event.
    add_controls = '<lambda>' # stores an anonymous function.
    response('<'controls>')  # configure the response of all controls.

    # EXAMPLE:
    self.on_resize.add_controls = lambda:self.new_control.response(self.on_resize.controls)  # we add all the controls
    ```

    """
    def __init__(self) -> None:
        self.__page: Page = None
        self.__height: float = None
        self.__width: float = None
        self.__add_def_control: function = None
        self.__add_controls: function = None
        self.__add_control: list = []

    def _call(self):
        return {'page': self._page, }

    @property
    def add_def_control(self):
        return self.__add_def_control

    @add_def_control.setter
    def add_def_control(self, control):
        self.__add_def_control = control

    async def _run_async(self) -> object:
        return await self.__add_def_control()

    def _run(self) -> object:
        return self.__add_def_control()

    @property
    def controls(self):
        return self.__add_control

    def add_control(self, control: object, height: int | float, max_height: int | float = None):
        _control = (control, height, max_height)
        self.__add_control.append(_control)

    @property
    def add_controls(self):
        return self.__add_controls

    @add_controls.setter
    def add_controls(self, controls):
        self.__add_controls = controls

    async def _response_run_async(self) -> object:
        return await self.__add_controls()

    def _response_run(self) -> object:
        return self.__add_controls()

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page):
        self.__page = page

    @property
    def height(self):
        if self.__height == None:
            return self.__page.height
        else:
            return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def width(self):
        if self.__width == None:
            return self.__page.width
        else:
            return self.__width

    @width.setter
    def width(self, width):
        self.__width = width


class MyController:
    """ 
    The Fast-Flet MyController class contains the following inheriting attributes.
    ```python
    self.call.model = None # It is assigned the class of the file.py in the models folder.
    self.call.on_resize = on_resize # It is assigned the self.call.on_resize of the View class from the file.py in the views folder.
    self.call.on_keyboard_event = on_keyboard # It is assigned the self.call.on_keyboard_event of the View class in the .py file in the views folder.
    self._x = _self # The custom control object is stored.
    self._user_control = None # The class that will be used in the custom control is stored.
    ```
    
    """

    def __init__(self, _self: object, on_resize: MyPageResize = None, on_keyboard: Mykeyboard = None) -> None:
        self.call = CallController()
        self.call.model = None
        self.call.on_resize = on_resize
        self.call.on_keyboard_event = on_keyboard
        self._x = _self
        self._user_control = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new):
        self._x = new

    @property
    def user_control(self):
        return self._user_control

    @user_control.setter
    def user_control(self, new):
        self._user_control = new

    async def response_async(self, conteiner: list):
        for value in conteiner:
            if value[2]:
                if self.call.on_resize.height >= int(value[2]):
                    value[0].height = self.call.on_resize.height - value[1]
                    await self.x.update_async()
            else:
                value[0].height = self.call.on_resize.height - value[1]
                await self.x.update_async()

    def response(self, conteiner: list):
        for value in conteiner:
            if value[2]:
                if self.call.on_resize.height >= int(value[2]):
                    value[0].height = self.call.on_resize.height - value[1]
                    self.x.update()
            else:
                value[0].height = self.call.on_resize.height - value[1]
                self.x.update()


class CallController:
    def __init__(self, model=None, on_keyboard_event=None, on_resize=None) -> None:
        self.__model = model
        self.__on_keyboard_event: Mykeyboard = on_keyboard_event
        self.__on_resize: MyPageResize = on_resize

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def on_keyboard_event(self):
        return self.__on_keyboard_event

    @on_keyboard_event.setter
    def on_keyboard_event(self, on_keyboard_event):
        self.__on_keyboard_event = on_keyboard_event

    @property
    def on_resize(self):
        return self.__on_resize

    @on_resize.setter
    def on_resize(self, on_resize):
        self.__on_resize = on_resize


@dataclass
class ConfView:
    """ 
    Note: if the parameter receives a flet class, it is used ```lambda```.

    USE:
    ```
    controls: list = None
    appbar: AppBar = None # use lambda
    floating_action_button: FloatingActionButton = None # use lambda
    navigation_bar: NavigationBar = None # use lambda
    vertical_alignment: MainAxisAlignment = None # use lambda
    horizontal_alignment: CrossAxisAlignment = None # use lambda
    spacing: int = None
    padding: int = None # use lambda
    bgcolor: str = None # use lambda
    # ScrollableControl specific
    scroll: ScrollMode = None # use lambda
    auto_scroll: bool = None
    fullscreen_dialog: bool = None
    on_scroll_interval: OptionalNumber = None # use lambda
    on_scroll = None
    ```
    -----
    EXAMPLE:
    ```
    view = ConfView(
        appbar=lambda: ft.AppBar(
            title=ft.Text("fast-flet"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(
                            text="Checked item", checked=False
                        ),
                    ]
                ),
            ],
        )
    )
    ```
    """
    controls: list = None
    appbar: AppBar = None
    floating_action_button: FloatingActionButton = None
    navigation_bar: NavigationBar = None
    vertical_alignment: MainAxisAlignment = None
    horizontal_alignment: CrossAxisAlignment = None
    spacing: int = None
    padding: int = None
    bgcolor: str = None
    # ScrollableControl specific
    scroll: ScrollMode = None
    auto_scroll: bool = None
    fullscreen_dialog: bool = None
    on_scroll_interval: OptionalNumber = None
    on_scroll = None


class ViewPage:
    """ 
    -> ```self.call````
    ```
    self.call.page: Page # receives the page from the main function
    self.call.route: str = '/' # establish a route (Automatic Routing)
    self.call.page_clear:bool = False # set removal of list page.views stored by flet (Automatic Routing)
    self.call.url_params: list = None # receives the parameters sent through the url
    self.call.is_login: bool = False # Establish if the page requires login.
    self.call.on_keyboard_event: Mykeyboard # receive information about the event: 'on_keyboard_event'
    self.call.on_resize: MyPageResize # receive information about the event: 'on_resize'
    ```
    ---
    -> configure flet View properties ```flet.View```
    ```
    self.controls: list = None
    self.appbar: AppBar = None
    self.floating_action_button: FloatingActionButton = None
    self.navigation_bar: NavigationBar = None
    self.vertical_alignment: MainAxisAlignment = None
    self.horizontal_alignment: CrossAxisAlignment = None
    self.spacing: int = None
    self.padding: int = None
    self.bgcolor: str = None
    # ScrollableControl specific
    self.scroll: ScrollMode = None
    self.auto_scroll: bool = None
    self.fullscreen_dialog: bool = None
    self.on_scroll_interval: int = None
    self.on_scroll = None
    ```
    ---
    Example:
    ```
    import flet as ft
    from Routing_flet import ViewPage

    
    class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/login' # we assign a url
        self.call.page_clear = True

    # required login configuration (default is None)
    def login_required(self) -> bool:
        super().login_required()
        class_login = Login() # import the login controller class
        add_login_required = lambda:class_login.login() #We use the method of the class where the login configuration has been made
        return add_login_required()
    
    # View general configuration
    def build(self):
        self.call.page.title = 'Login'
        self.appbar.title = ft.Text('Login')

        self.controls=[
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text('LOGIN',size=30),
                                    ft.FilledButton(
                                        'ir a index',
                                        on_click=lambda e:e.page.go('/index')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=450,
                            height=450,
                            bgcolor=ft.colors.BLACK12,
                            alignment=ft.alignment.center,
                            border_radius=20

                        ),

                    ]
                )
            ]
        
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment  = ft.MainAxisAlignment.CENTER
    ``` 
    """

    def __init__(self) -> None:
        self.call = CallView()
        self.__view = None
        self._route: str = None
        self.controls: list = None
        self.appbar: AppBar = None
        self.floating_action_button: FloatingActionButton = None
        self.navigation_bar: NavigationBar = None
        self.vertical_alignment: MainAxisAlignment = None
        self.horizontal_alignment: CrossAxisAlignment = None
        self.spacing: int = None
        self.padding: int = None
        self.bgcolor: str = None

        # ScrollableControl specific

        self.scroll: ScrollMode = None
        self.auto_scroll: bool = None
        self.fullscreen_dialog: bool = None
        self.on_scroll_interval: int = None
        self.on_scroll = None

    def login_required(self) -> bool:
        return None

    def build(self):
        pass

    def _run_view(self):
        self.build()
        self.__view = View(
            route=self._route,
            controls=self.controls,
            appbar=self.appbar,
            floating_action_button=self.floating_action_button,
            navigation_bar=self.navigation_bar,
            vertical_alignment=self.vertical_alignment,
            horizontal_alignment=self.horizontal_alignment,
            spacing=self.spacing,
            padding=self.padding,
            bgcolor=self.bgcolor,
            #
            # ScrollableControl specific
            #
            scroll=self.scroll,
            auto_scroll=self.auto_scroll,
            fullscreen_dialog=self.fullscreen_dialog,
            on_scroll_interval=self.on_scroll_interval,
            on_scroll=self.on_scroll
        )

    async def _view_async(self):
        return self.__view

    def _view(self):
        return self.__view


class CallView:
    def __init__(self) -> None:
        self.__page: Page = None
        self.__route: str = '/'
        self.__page_clear = False
        self.__url_params: list = None
        self.__is_login: bool = False
        self.__on_keyboard_event: Mykeyboard = None
        self.__on_resize: MyPageResize = None

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page: object):
        self.__page = page

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, route: str):
        self.__route = route

    @property
    def page_clear(self):
        return self.__page_clear

    @page_clear.setter
    def page_clear(self, page_clear: bool):
        self.__page_clear = page_clear

    @property
    def url_params(self):
        return self.__url_params

    @url_params.setter
    def url_params(self, url_params: dict):
        self.__url_params = url_params

    @property
    def user_control(self):
        return self.__user_control

    @user_control.setter
    def user_control(self, user_control: object):
        self.__user_control = user_control

    @property
    def is_login(self):
        return self.__is_login

    @is_login.setter
    def is_login(self, is_login: bool):
        self.__is_login = is_login

    # events
    @property
    def on_keyboard_event(self):
        return self.__on_keyboard_event

    @on_keyboard_event.setter
    def on_keyboard_event(self, on_keyboard_event: object):
        self.__on_keyboard_event = on_keyboard_event

    @property
    def on_resize(self):
        return self.__on_resize

    @on_resize.setter
    def on_resize(self, on_resize: object):
        self.__on_resize = on_resize


def add_view(url: str, view: ViewPage, clear: bool = True) -> dict:
    """
        -> Add flet ```page.views```
        
        USE:
        ```
        add_view(
            url='/task', # we set the url
            view=Taskview(), # We use the class imported from the views folder
            clear=False # All views stored in 'page.views' are removed (default is true)
            )
        ```
        ---
        Example:
        ```
        add_routes(
            [
                add_view(url='/index',view=View()),
                add_view(url='/task',view=Taskview(),clear=False),
                add_view(url='/counter/:id/:name',view=ContadorView(), clear=False),
                add_view(url='/login',view=LoginView()),
                add_view(url='/resize',view=ResizeView(), clear=False),
                add_view(url='/404-fast-flet',view=Page_404View(), clear=False),
            ]
        )
        ```
        """
    return {'url': url, 'view': view, 'clear': clear}
