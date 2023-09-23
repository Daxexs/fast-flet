from fast_flet import ViewPage
import flet as ft
from controllers.resize import TestResizeC


class TestResize(ft.UserControl):
    def __init__(self, page: ft.Page, on_resize):
        super().__init__()
        self.page = page
        self.new_control = TestResizeC(self, on_resize)
        self.on_resize = on_resize # on_resize values ​​are obtained
        self.on_resize.add_def_control = lambda: self.new_control.resize() # add a function that will be executed with the on_resize event

        self.height_r = ft.Text(
            f'HEIGHT: {self.page.height}'
        )
        self.width_r = ft.Text(
            f'WIDTH: {self.page.width}'
        )

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        'ON RESIZE',
                        size=30,
                        color=ft.colors.RED_600,
                        weight=ft.FontWeight.BOLD
                    ),
                    self.height_r,
                    self.width_r
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor=ft.colors.BLUE_500,
            height=150,
            width=200,
            alignment=ft.alignment.center,
            border_radius=10
        )

class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/resize' # we assign a url
        self.call.is_login = True # requires login to access the page (previously configured)

    # View general configuration
    def build(self):
        page = self.call.page
        on_resize = self.call.on_resize

        page.title = 'Resize'

        test_resize = TestResize(page, on_resize)

        # modify View properties : https://flet.dev/docs/controls/view
        self.appbar.title = ft.Text('Resize')

        self.controls = [
            test_resize
        ]

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
