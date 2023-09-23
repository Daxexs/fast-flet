import flet as ft
from fast_flet import ViewPage


class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/404-fast-flet' # we assign a url with parameters that we are going to receive 

    # View general configuration
    def build(self):

        page = self.call.page
        page.title = 'page 404'

        # modify View properties : https://flet.dev/docs/controls/view

        self.controls = [
            ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text('404: fast-flet', size=50),
                                ft.Text('url not found'),
                                ft.FilledButton(
                                    'go Home',
                                    width=200,
                                    height=40,
                                    on_click=lambda e:e.page.go('/index'),
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.AMBER_300,
                                        color=ft.colors.WHITE70
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.BLACK12,
                        padding=20,
                        border_radius=10,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )

        ]

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
