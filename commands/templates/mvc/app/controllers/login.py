import flet as ft
#from fast_flet import MyController,MyPageResize
import random

class Login():
    def __init__(self) -> None:
        pass
    
    def login(self):
        a = True
        b = False
        test = [a,b,a,b,a,b,a,b,a,b,a,b,a,b]
        resultado = test[random.randint(0,10)]
        print(f'check url permission: {resultado}')
        return resultado
