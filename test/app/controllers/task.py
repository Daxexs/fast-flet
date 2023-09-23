from fast_flet import MyController,MyPageResize,Mykeyboard
import flet as ft
from time import sleep

# view 'Task' class controller
class TaskC(MyController):
    def __init__(self, _self: object, on_resize: MyPageResize = None, on_keyboard: Mykeyboard = None) -> None:
        super().__init__(_self, on_resize, on_keyboard)

    def delete(self, e):
        self.x.delet(self.x)

    def edit(self,e):
        self.x.task.visible = False
        self.x.edit.visible = False
        self.x.delete.visible = False

        self.x.edit_task.visible = True
        self.x.edit_save.visible = True

        self.x.edit_task.value = self.x.task.value
        self.x.update()

    def _save(self):
        if self.x.edit_task.value:
            self.x.task.value = self.x.edit_task.value
            self.x.edit_task.visible = False
            self.x.edit_save.visible = False
    
            self.x.task.visible = True
            self.x.edit.visible = True
            self.x.delete.visible = True
            self.x.update()

    def save(self,e):
        self._save()

    # used with keyboard input
    def keep_on_keyboard(self):
        keyboard = self.call.on_keyboard_event
        if keyboard.key() == 'K' and keyboard.alt():
           self._save()

# view's ContentTask class handler
class ContentTaskC(MyController):
    def __init__(self, _self: object, on_resize: MyPageResize = None, on_keyboard=None) -> None:
        super().__init__(_self, on_resize, on_keyboard)
    
    def _add_task(self):
        if self.x.input.value != '':
            input_task = self.x.input.value
            task = self.user_control(self.delete, input_task, self.call.on_keyboard_event)
            self.x.colum_task.controls.append(task)
            self.x.input.value = ''
            self.x.input.label = 'Enter a task'
        else:
            self.x.input.label = 'Enter a task please'
            self.x.input.border_color=ft.colors.RED
            self.x.update()
            sleep(2)
            self.x.input.border_color=None
        self.x.update()

    def add_task(self,e):
        self._add_task()

    def delete(self, task):
        self.x.colum_task.controls.remove(task)
        self.x.update()
    
    def update_input(self,e):
        self.x.input.border_color=None
        self.x.update()
    
    # used with keyboard input
    def add_on_keyboard(self):
        keyboard = self.call.on_keyboard_event
        if keyboard.key() == 'L' and keyboard.alt():
            self._add_task()