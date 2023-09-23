from flet import Page, RouteChangeEvent, KeyboardEvent, ControlEvent, View

from .getInformation import STRUCTURE, routing
from .inheritance import Mykeyboard, MyPageResize, ViewPage
from .view_404 import ViewError
from .view_404_async import ViewErrorAsync
from rich import print as pt
from repath import match

routing_pages = routing()

class RoutePage:

    """
    Class usage:
    ```
    RoutePage(
        page=page, # parameter of the main function of the app or website
        route="/index", # path where the app or website will be initialized
        route_login='/login', # login route, where it will be redirected
        route_404="/404-fast-flet", # custom page path not found.
        view=view, # general configuration of all the 'View' of the page '(page.views)'
        manual_routing=  # Use manual routing of 'views'
    )
    ```
    -----
    Example:
    ```
    def main(page: ft.Page):
        # CONFIGURACION GENERAL
        page.title = 'fast-flet'

        # ROUTING AND HANDLING VIEWS IN AUTOMATICO
        fast_flet = RoutePage(
            page=page,
            route="/index",
        )

        # WE RUN THE ROUTING OF THE VIEWS
        fast_flet.run()

    ft.app(main,
        port=8000,
        view=ft.AppView.WEB_BROWSER,
        web_renderer=ft.WebRenderer.AUTO,
        route_url_strategy='hash'
       )
    ```
    """

    def __init__(self, page: Page, route: str, route_login: str = None, route_404: str = None, view: View = None, manual_routing: bool = False):
        self.__page = page
        self.__conf_view = view
        self.__keyboard_on = Mykeyboard()
        self.__page_on_resize = MyPageResize()
        self.__page_on_resize.page = self.__page

        self.__route = route
        self.__route_login = route_login
        self.__route_404_edit = route_404
        self.__route_404: str = None
        self.__view_404 = ViewError()
        self.__view_404_async = ViewErrorAsync()
        self.__manual_routing = manual_routing
        self.__route_page = None
        self.__STRUCTURE: list = STRUCTURE

        self.__url_init()

    def __url_init(self):
        if self.__page.route == "/":
            self.__page.route = self.__route
        if self.__route_login == None:
            self.__route_login = self.__route
        if self.__route_404_edit == None:
            self.__route_404 = self.__view_404.route
            self.__view_404.route_index = self.__route
            self.__view_404_async.route_index = self.__route
        else:
            self.__route_404 = self.__route_404_edit
        if not self.__manual_routing:
            self.__route_page = routing_pages

        if len(self.__page.views) == 1:
            self.__page.views.clear()

    def __route_change(self, route: RouteChangeEvent):
        pg_404 = True
        self.__page_on_resize.add_controls = None
        self.__page_on_resize.add_def_control = None
        self.__keyboard_on.controls.clear()

        for url, view in self.__route_page.items():
            clear_view = view['clear']
            view = view['view']
            route_math = match(url, route.route)
            if route_math:
                pg_404 = False

                try:
                    if view.call.is_login:
                        if self.__view.login_required():
                            if clear_view:
                                self.__page.views.clear()
                            view.call.url_params = route_math.groupdict()
                            self.__add_events_params(view, url)
                            break
                        elif self.__view.login_required() == None:
                            pt(f"[red]>> You have activated route protection -> '{url}' | but it is not configured![/red]")
                        else:
                            self.__page.go(self.__route_login)
                            break
                    else:
                        if clear_view:
                            self.__page.views.clear()
                        view.call.url_params = route_math.groupdict()
                        self.__add_events_params(view, url)
                        break
                except Exception as e:
                    raise e

        if pg_404:
            if self.__route_404_edit != None:
                assert self.__route_page[self.__route_404], "add the view of route 404, in the 'add_routes' function"
                page = self.__route_page[self.__route_404]
                view = page[self.__STRUCTURE[0]]
                self.__add_events_params(view, self.__route_404)
            else:
                self.__page.views.append(self.__view_404.view(self.__page))

        self.__page.update()

    def __add_view_atributes(self, view: ViewPage, route: str):
        view._route = route
        view.controls = self.__conf_view.controls
        view.appbar = self.__conf_view.appbar() if self.__conf_view.appbar else None
        view.floating_action_button = self.__conf_view.floating_action_button(
        ) if self.__conf_view.floating_action_button else None
        view.navigation_bar = self.__conf_view.navigation_bar(
        ) if self.__conf_view.navigation_bar else None
        view.vertical_alignment = self.__conf_view.vertical_alignment(
        ) if self.__conf_view.vertical_alignment else None
        view.horizontal_alignment = self.__conf_view.horizontal_alignment(
        ) if self.__conf_view.horizontal_alignment else None
        view.spacing = self.__conf_view.spacing
        view.padding = self.__conf_view.padding() if self.__conf_view.padding else None
        view.bgcolor = self.__conf_view.bgcolor() if self.__conf_view.bgcolor else None

        # ScrollableControl specific
        view.scroll = self.__conf_view.scroll() if self.__conf_view.scroll else None
        view.auto_scroll = self.__conf_view.auto_scroll
        view.fullscreen_dialog = self.__conf_view.fullscreen_dialog
        view.on_scroll_interval = self.__conf_view.on_scroll_interval(
        ) if self.__conf_view.on_scroll_interval else None
        view.on_scroll = self.__conf_view.on_scroll

    def __add_events_params(self, view: ViewPage, route: str):
        view.call.page = self.__page
        view.call.on_keyboard_event = self.__keyboard_on
        view.call.on_resize = self.__page_on_resize
        if self.__conf_view:
            self.__add_view_atributes(view, route)
        else:
            view._route = route

        view._run_view()
        self.__page.views.append(view._view())

    def __view_pop(self, e):
        self.__page.views.pop()
        top_view = self.__page.views[-1]
        self.__page.go(top_view.route)

    def __on_keyboard(self, e: KeyboardEvent):
        self.__keyboard_on.call = e
        if len(self.__keyboard_on.controls) != 0:
            self.__keyboard_on._run_controls()

    def __page_resize(self, e: ControlEvent):
        self.__page_on_resize.width = e.control.width
        self.__page_on_resize.height = e.control.height

        if self.__page_on_resize.add_def_control != None:
            self.__page_on_resize._run()
        if self.__page_on_resize.add_controls != None:
            self.__page_on_resize._response_run()

    def run(self):
        """
        -> ```Initialize fast-flet```
        """
        assert self.__route_page, "Manual routes are activated (deactivate) in 'RoutePage' or add manual routes 'add_routes'"
        self.__view: ViewPage = self.__route_page[self.__route_login]['view']
        self.__page.on_route_change = self.__route_change
        self.__page.on_view_pop = self.__view_pop
        self.__page.on_resize = self.__page_resize
        self.__page.on_keyboard_event = self.__on_keyboard
        self.__page.on_error = lambda e: print("Page error:", e.data)
        self.__page.go(self.__page.route)
        pt(f"[green]>> Reload session: {self.__page.session_id}[/green]")

    # async ---------

    async def __route_change_async(self, route: RouteChangeEvent):
        pg_404 = True
        self.__page_on_resize.add_controls = None
        self.__page_on_resize.add_def_control = None
        self.__keyboard_on.controls.clear()

        for url, view in self.__route_page.items():
            clear_view = view['clear']
            view = view['view']
            route_math = match(url, route.route)
            if route_math:
                pg_404 = False

                try:
                    if view.call.is_login:
                        if self.__view.login_required():
                            if clear_view:
                                self.__page.views.clear()
                            view.call.url_params = route_math.groupdict()
                            await self.__add_events_params_async(view, url)
                            break
                        elif self.__view.login_required() == None:
                            pt(f"[red]>> You have activated route protection -> '{url}' | but it is not configured![/red]")
                        else:
                            await self.__page.go_async(self.__route_login)
                            break
                    else:
                        if clear_view:
                            self.__page.views.clear()
                        view.call.url_params = route_math.groupdict()
                        await self.__add_events_params_async(view, url)
                        break
                except Exception as e:
                    raise e

        if pg_404:
            if self.__route_404_edit != None:
                assert self.__route_page[self.__route_404], "add the view of route 404, in the 'add_routes' function"
                page = self.__route_page[self.__route_404]
                view = page[self.__STRUCTURE[0]]
                await self.__add_events_params_async(view, self.__route_404)
            else:
                self.__page.views.append(self.__view_404_async.view(self.__page))

        await self.__page.update_async()

    async def __add_view_atributes_async(self, view: ViewPage, route: str):
        view._route = route
        view.controls = self.__conf_view.controls
        view.appbar = self.__conf_view.appbar
        view.floating_action_button = self.__conf_view.floating_action_button
        view.navigation_bar = self.__conf_view.navigation_bar
        view.vertical_alignment = self.__conf_view.vertical_alignment
        view.horizontal_alignment = self.__conf_view.horizontal_alignment
        view.spacing = self.__conf_view.spacing
        view.padding = self.__conf_view.padding
        view.bgcolor = self.__conf_view.bgcolor

        # ScrollableControl specific
        view.scroll = self.__conf_view.scroll
        view.auto_scroll = self.__conf_view.auto_scroll
        view.fullscreen_dialog = self.__conf_view.fullscreen_dialog
        view.on_scroll_interval = self.__conf_view.on_scroll_interval
        view.on_scroll = self.__conf_view.on_scroll

    async def __add_events_params_async(self, view: ViewPage, route: str):
        view.call.page = self.__page
        view.call.on_keyboard_event = self.__keyboard_on
        view.call.on_resize = self.__page_on_resize
        if self.__conf_view != None:
            await self.__add_view_atributes_async(view, route)
        else:
            view._route = route
        view._run_view()
        self.__page.views.append(await view._view_async())

    async def __view_pop_async(self, e):
        self.__page.views.pop()
        top_view = self.__page.views[-1]
        await self.__page.go_async(top_view.route)

    async def __on_keyboard_async(self, e: KeyboardEvent):
        self.__keyboard_on.call = e
        if len(self.__keyboard_on.controls) != 0:
            await self.__keyboard_on._run_controls_async()

    async def __page_resize_async(self, e: ControlEvent):
        self.__page_on_resize.width = e.control.width
        self.__page_on_resize.height = e.control.height

        if self.__page_on_resize.add_def_control != None:
            await self.__page_on_resize._run_async()
        if self.__page_on_resize.add_controls != None:
            await self.__page_on_resize._response_run_async()

    async def run_async(self):
        """
        -> ```Initialize fast-flet in async```
        """
        assert self.__route_page, "Manual routes are activated (deactivate) in 'RoutePage'"
        self.__view: ViewPage = self.__route_page[self.__route_login]['view']
        self.__page.on_route_change = self.__route_change_async
        self.__page.on_view_pop = self.__view_pop_async
        self.__page.on_resize = self.__page_resize_async
        self.__page.on_keyboard_event = self.__on_keyboard_async
        self.__page.on_error = lambda e: print("Page error:", e.data)
        await self.__page.go_async(self.__page.route)
        pt(f"[green]>>async: Reload session: {self.__page.session_id}[/green]")

    def add_routes(self, add_views: list):
        """
        -> Add flet ```page.views```
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
        routing = {}
        for i in add_views:
            url = i['url']
            routing[url] = {}
            routing[url]['view'] = i['view']
            routing[url]['clear'] = i['clear']

        self.__route_page = routing
        assert len(add_views) != 0, "add view (add_view) in 'add_routes'"
        assert self.__route_page.get(
            self.__route_login), "add view login (add_view) in 'add_routes'"
        self.__view: ViewPage = self.__route_page[self.__route_login]['view']
