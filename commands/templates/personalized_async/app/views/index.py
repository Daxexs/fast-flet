import flet as ft
from fast_flet import ViewPage


class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/index'
        self.call.page_clear = True  # remove icon return to previous view of 'appbar', if it is activated

    async def contador(self, e):
        await self.call.page.go_async('/counter/100/fast-flet')

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
                                ft.Text("welcome to Fast-Flet", size=50),
                                ft.FilledButton(
                                    'Test 404 error',
                                    on_click=self.contador
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        width=550,
                        height=450,
                        bgcolor='blue800',
                        alignment=ft.alignment.center,
                        border_radius=20

                    ),

                ]
            )
        ]
        
        self.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        self.vertical_alignment=ft.MainAxisAlignment.CENTER