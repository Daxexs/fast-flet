import flet as ft
import asyncio
from fast_flet import ViewPage
from controllers import ContadorC

class Contador(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.new_control = ContadorC(self) # # We create an object of the controller class of this class, to be able to use its methods.

    def build(self):
        self.test = 'test inicio'
        self.numero = ft.TextButton(
            '0',
            style=ft.ButtonStyle(
                bgcolor=ft.colors.BLACK12
            )
        )
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        ft.icons.REMOVE,
                        on_click=self.new_control.min,  # Al enviar self estamos enviando la clase
                        bgcolor=ft.colors.RED_400
                    ),
                    self.numero,
                    ft.IconButton(
                        ft.icons.ADD,
                        on_click=self.new_control.max,
                        bgcolor=ft.colors.GREEN_400
                    ),
                ],
                alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor=ft.colors.BLACK26,
            border_radius=10,
            padding=20,
            width=200,
            alignment=ft.alignment.center
        )
    

class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/counter/:id/:name' # we assign a url with parameters that we are going to receive
    
    # View general configuration
    def build(self):

        # get the url parameters
        # print('url params:', self.call.url_params)

        page = self.call.page
        page.title = 'Counter'
        contador1 = Contador()
        contador2 = Contador()
        contador3 = Contador()

        # modify View properties : https://flet.dev/docs/controls/view
        self.appbar.title = ft.Text('Counter')

        self.controls=[
                contador1,
                contador2,
                contador3,
                ft.TextButton('go home',on_click= lambda e:e.page.go('/index'))

            ]
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment  = ft.MainAxisAlignment.CENTER
