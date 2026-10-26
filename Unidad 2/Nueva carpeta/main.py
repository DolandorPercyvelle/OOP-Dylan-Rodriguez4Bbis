from tkinter import Tk

from inicio_sesión import Authentication
from registro import UserModel
from style import LoginView


class System:
    def __init__(self):
        self.root = Tk()
        self.vista = LoginView(self.root)
        self.modelo = UserModel()
        self.controlador = Authentication(self.modelo, self.vista)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.start()
