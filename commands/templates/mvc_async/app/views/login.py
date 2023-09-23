import flet as ft
from fast_flet import ViewPage
from controllers.login import Login


class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/login' # we assign a url
        self.call.page_clear = True

    # required login configuration
    def login_required(self) -> bool:
        super().login_required()
        class_login = Login() # import the login controller class
        add_login_required = lambda:class_login.login() #We use the method of the class where the login configuration has been made
        return add_login_required()
    
    async def index_go(self, e):
        await self.call.page.go_async('/index')
    
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
                                        on_click=self.index_go
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