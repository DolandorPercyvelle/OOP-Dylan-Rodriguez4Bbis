import tkinter as tk
from tkinter import messagebox

from Models.login_model import AuthenticationServiceError, authenticate
from Views.home_view import welcome_screen


class login_screen:
    def __init__(self, root, authenticator=authenticate):
        self.root = root
        self.authenticator = authenticator
        self.root.title("System Lab 7")
        self.root.geometry("340x240")
        self.root.resizable(False, False)

        tk.Label(root, text="Iniciar sesion", font=("Arial", 16, "bold")).pack(
            pady=(24, 16)
        )
        tk.Label(root, text="Usuario").pack(anchor="w", padx=40)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(fill="x", padx=40, pady=(2, 10))
        tk.Label(root, text="Contrasena").pack(anchor="w", padx=40)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(fill="x", padx=40, pady=(2, 14))
        self.login_button = tk.Button(root, text="Login", command=self.auth)
        self.login_button.pack()
        self.username_entry.focus_set()
        self.root.bind("<Return>", lambda _event: self.auth())

    def auth(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror(
                "Login", "Introduce usuario y contrasena.", parent=self.root
            )
            return

        self.login_button.configure(state="disabled")
        try:
            authenticated = self.authenticator(username, password)
        except AuthenticationServiceError:
            messagebox.showerror(
                "Error de conexion",
                "No se pudo verificar el acceso. Comprueba la configuracion de la base de datos.",
                parent=self.root,
            )
            return
        finally:
            self.login_button.configure(state="normal")

        if not authenticated:
            messagebox.showerror(
                "Login", "Usuario o contrasena incorrectos.", parent=self.root
            )
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()
            return

        for child in self.root.winfo_children():
            child.destroy()
        self.root.unbind("<Return>")
        welcome_screen(self.root, username)
