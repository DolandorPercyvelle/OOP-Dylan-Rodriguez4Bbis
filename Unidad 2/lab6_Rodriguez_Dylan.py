import tkinter as tk

import os
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class SmartSpeaker(SmartDevice):
    def __init__(self, name):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name}, is playing bluegrass music at volume 20%"

    def turn_off(self):
        return f"{self.name} is OFF. Goodbye!"


class SmartTv(SmartDevice):
    def __init__(self, name):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name} is ON. Enjoy your TV Shows"

    def turn_off(self):
        return f"{self.name} is OFF. Goodbye!"


class SmartWatch(SmartDevice):
    def __init__(self, name):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name} is ON. Enjoy your Watch"

    def turn_off(self):
        return f"{self.name} is OFF. Goodbye!"


class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)

    def turn_on(self):
        return f"{self.name} is ON. Brighten up your space!"

    def turn_off(self):
        return f"{self.name} is OFF. Goodbye!"


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Lab 6: Polymorphism with GUI")
        self.geometry("480x660")
        self.resizable(False, False)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, "icon.png")

        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file=icon_dir)
            self.iconphoto(True, self.app_icon)
        else:
            print("the file does not exists")

        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "TV": SmartTv("Hisense Smart TV"),
            "Speaker": SmartSpeaker("Echo Dot 5"),
            "Light": SmartLight("Smart Light"),
            "Watch": SmartWatch("Apple Watch Series 9")

        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="POLYMORPHISM",
            font=("Arial", 22, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = tk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="Turn On Device",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        btn_action = tk.Button(
            self,
            text="Turn Off Device",
            command=self._handle_off,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        # Activity Log
        log_box = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=8
        )
        log_box.pack(fill="both", expand=True, padx=20, pady=8)

        self.activity_log = tk.Listbox(
            log_box,
            height=6,
            font=("Arial", 9),
            activestyle="none"
        )
        self.activity_log.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(log_box, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        self.activity_log.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.activity_log.yview)

    def _display_result(self, result_message):
        self.lbl_output.config(
            text=result_message,
            font=("Arial", 10, "normal")
        )
        self.activity_log.insert(tk.END, result_message)
        self.activity_log.see(tk.END)

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_on()

        # 4. Display and record the result
        self._display_result(result_message)

    def _handle_off(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_off()

        # 4. Display and record the result
        self._display_result(result_message)


# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
