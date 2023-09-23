from fast_flet import MyController,MyPageResize,Mykeyboard

class TestResizeC(MyController):
    def __init__(self, _self: object, on_resize: MyPageResize = None, on_keyboard: Mykeyboard = None) -> None:
        super().__init__(_self, on_resize, on_keyboard)
    
    async def resize(self):
        v = self.call.on_resize # we get the values ​​of on_resize
        self.x.height_r.value = f'HEIGHT: {v.height}'
        self.x.width_r.value = f'WIDTH: {v.width}'
        await self.x.update_async()