import tkinter as tk

class BotonGeneral(tk.Button):
    def __init__(self, master, text, funcion=None, **kwargs):
        super().__init__(master, text=text, **kwargs)

        self.config(
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=0,
        )

        if funcion:
            self.config(command=funcion)