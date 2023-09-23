import flet as ft

class ViewErrorAsync:
    def __init__(self) -> None:
        self.route = '/404-Routing-Flet'
        self.route_index = None
    
    
    def view(self, page: ft.Page):

        page.title = 'page 404'
        async def go_index(e):
            await page.go_async(self.route_index)

        return ft.View(
            self.route,
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text('404', size=90),
                                    ft.Text('url no encontrada:'),
                                    ft.FilledButton(
                                        'ir a Home',
                                        width=200,
                                        height=40,
                                        on_click=go_index,
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.colors.AMBER_300,
                                            color=ft.colors.WHITE70
                                        )
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            bgcolor=ft.colors.LIGHT_BLUE_500,
                            padding=20,
                            border_radius=10,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                )

            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
