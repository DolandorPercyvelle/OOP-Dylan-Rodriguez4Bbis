import tkinter as tk


class welcome_screen:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Bienvenido")
        self.root.geometry("360x220")
        self.root.resizable(False, False)
        tk.Label(
            root,
            text=f"Bienvenido, {username}!",
            font=("Arial", 18, "bold"),
        ).pack(expand=True)
