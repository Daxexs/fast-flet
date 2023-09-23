from fast_flet import ViewPage, MyPageResize, Mykeyboard
import flet as ft
from controllers.task import TaskC, ContentTaskC


class Task(ft.UserControl):
    def __init__(self, delete, input_task: str, on_keyboard: Mykeyboard) -> None:
        super().__init__()
        self.new_control = TaskC(self, on_keyboard=on_keyboard)
        self.delet = delete
        self.input_task = input_task
        self.on_keyboard = on_keyboard
        # add a function to on_keyboard, which will be executed according to what is established in the function, it will be executed with keyboard input.
        self.on_keyboard.add_control(self.new_control.keep_on_keyboard)

        self.task = ft.TextField(
            col=8,
            value=self.input_task,
            multiline=True,
        )
        self.edit = ft.IconButton(
            ft.icons.EDIT,
            col=2,
            on_click=self.new_control.edit,
            icon_color=ft.colors.GREEN_500
        )

        self.delete = ft.IconButton(
            ft.icons.DELETE,
            col=2,
            on_click=self.new_control.delete,
            icon_color=ft.colors.RED_500
        )

        self.edit_task = ft.TextField(
            col=10,
            visible=False,
            multiline=True,
            autocorrect=True,
            helper_text="'Alt'+'K' -> to save task"
        )
        self.edit_save = ft.IconButton(
            icon=ft.icons.SAVE,
            col=2,
            icon_color=ft.colors.GREEN_400,
            on_click=self.new_control.save,
            visible=False
        )

        self.edit_container = ft.ResponsiveRow(
            [
                self.edit_task,
                self.edit_save
            ],
            col=12
        )

    def build(self):
        return ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    self.task,
                    self.edit,
                    self.delete,
                    self.edit_task,
                    self.edit_save,
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            bgcolor=ft.colors.BLACK26,
            border_radius=10,
            padding=20,
            border=ft.border.all(width=4, color=ft.colors.WHITE10)

        )


class ContentTask(ft.UserControl):
    def __init__(self, on_resize: MyPageResize, on_keyboard: Mykeyboard):
        super().__init__()
        # We create an object of the controller class of this class, to be able to use its methods.
        self.new_control = ContentTaskC(self, on_resize, on_keyboard)
        self.on_keyboard = on_keyboard  # the values ​​of on_keyboard_event are obtained
        # add a function to on_keyboard, which will be executed according to what is established in the function, it will be executed with keyboard input.
        self.on_keyboard.add_control(self.new_control.add_on_keyboard)
        self.on_resize = on_resize  # on_resize values ​​are obtained
        self.new_control.user_control = Task # # We send the class that we are going to use in the controller of this class
       
        self.input = ft.TextField(
            col=8,
            label='Enter the task',
            multiline=True,
            autocorrect=True,
            helper_text="'Alt'+'L' -> to add task",
            on_focus=self.new_control.update_input,

        )
        self.colum_task = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)

        self.response_page = ft.Container(
            col={'sm': 5},
            bgcolor=ft.colors.BLACK26,
            height=self.on_resize.height - 80,
            padding=10,
            border_radius=10
        )

        self.response_task = ft.Container(
            col={'sm': 11},
            bgcolor=ft.colors.BLACK12,
            height=self.on_resize.height-244,
            padding=10,
            border_radius=10,

        )

        # We add the controllers that are height responsive, if it is not displayed the page has to be reloaded (possible flet error)
        self.on_resize.add_control(self.response_page, 80, 420)
        self.on_resize.add_control(self.response_task, 244, 383)
        self.on_resize.add_controls = lambda: self.new_control.response_async(
            self.on_resize.controls)  # we add all the controls

    def build(self):
        self.response_task.content = self.colum_task
        self.response_page.content = ft.ResponsiveRow(
            controls=[
                ft.Text('Task', size=25,
                        text_align=ft.TextAlign.CENTER),
                ft.ResponsiveRow(
                    controls=[
                        self.input,
                        ft.FilledButton(
                            'ADD',
                            col=4,
                            on_click=self.new_control.add_task
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                self.response_task
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        return ft.ResponsiveRow(
            controls=[
                self.response_page
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )


class View(ViewPage):
    def __init__(self) -> None:
        super().__init__()
        self.call.route = '/task'  # we assign a url

    # View general configuration
    def build(self):
        self.route = '/task'

        # ------
        # We configure all the values ​​of the page.
        page = self.call.page  # we get all the values ​​of the page.
        page.title = 'Task'
        # --------

        on_resize = self.call.on_resize  # on_resize values ​​are obtained
        # the values ​​of on_keyboard_event are obtained
        on_keyboard = self.call.on_keyboard_event
        task = ContentTask(on_resize, on_keyboard)

        # modify View properties : https://flet.dev/docs/controls/view
        self.appbar.title = ft.Text('Task')

        self.controls = [
            task
        ]
