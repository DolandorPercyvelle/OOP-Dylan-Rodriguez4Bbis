import tkinter as tk

from Views.login_view import login_screen


def main():
    root = tk.Tk()
    login_screen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
