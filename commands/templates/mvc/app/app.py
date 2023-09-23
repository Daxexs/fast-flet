import flet as ft
from fast_flet import RoutePage, ConfView

# Import the View classes from the views folder to use in add_routes
""" from views.index import View
from views.contador import View as ContadorView
from views.login import View as LoginView """


def main(page: ft.Page):
    # SETTING GENERAL
    theme = ft.Theme()
    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    page.theme = theme
   
    # View flet configuration in all views
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

    # ROUTING AND HANDLING VIEWS IN AUTOMATICO
    fast_flet = RoutePage(
        page=page,
        route="/index",
        route_login='/login',
        view=view,
        #manual_routing= True
    )

    # ROUTING AND MANAGEMENT VIEWS IN MANUAL'
    """ fast_flet.add_routes(
        [
            add_view(url='/index',view=View()),
            add_view(url='/counter/:id/:name',view=ContadorView(), clear=False),
            add_view(url='/login',view=LoginView()),
        ]
    ) """

    # WE RUN THE ROUTING OF THE VIEWS
    fast_flet.run()


ft.app(main,
       port=8000,
       view=ft.AppView.WEB_BROWSER,
       assets_dir="assets",
       web_renderer=ft.WebRenderer.AUTO,
       route_url_strategy='hash'
       )