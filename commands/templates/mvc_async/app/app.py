import flet as ft
import flet_fastapi
from fast_flet import RoutePage, ConfView, add_view
import os

# Import the View classes from the views folder to use in add_routes
from views.index import View
from views.contador import View as ContadorView
from views.login import View as LoginView

async def main(page: ft.Page):
    # CONFIGURACION GENERAL
    theme = ft.Theme()
    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    page.title = "fast-flet"
    page.theme = theme

    # View flet configuration in all views
    view = ConfView(
        appbar=ft.AppBar(
            title=ft.Text("AppBar Example"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
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
        manual_routing= True
    )
    

    # ROUTING AND MANAGEMENT VIEWS IN MANUAL'
    fast_flet.add_routes(
        [
            add_view(url='/index',view=View()),
            add_view(url='/counter/:id/:name',view=ContadorView(), clear=False),
            add_view(url='/login',view=LoginView()),
        ]
    )

    # WE RUN THE ROUTING OF THE VIEWS IN ASYNC
    await fast_flet.run_async()


assets = os.path.abspath('./assets')
app = flet_fastapi.app(main,
                       assets_dir=assets,
                       app_name='fast-flet',
                       app_short_name='fast-flet-short',
                       app_description='fast-flet-descripcion',
                       web_renderer=ft.WebRenderer.AUTO,
                       route_url_strategy='hash',
                       )