import flet as ft
from fast_flet import ViewPage


class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/index'
        # remove icon return to previous view of 'appbar', if it is activated
        self.call.page_clear = True # clean the list of views added to the page (default is false)

    # View general configuration
    def build(self):
        # we assign a url
        self.route = '/index'
        page = self.call.page
        page.title = 'Index'

        # modify View properties : https://flet.dev/docs/controls/view
        self.appbar.title = ft.Text('Home')
        self.controls = [
            ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.FilledButton(
                                    'go Counter',
                                    on_click=lambda e: e.page.go(
                                        '/counter/100/fast-flet')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        width=450,
                        height=450,
                        bgcolor='blue800',
                        alignment=ft.alignment.center,
                        border_radius=20

                    ),

                ]
            )
        ]

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.bgcolor = ft.colors.BLACK
