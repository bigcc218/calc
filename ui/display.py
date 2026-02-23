import tkinter as tk

class Display(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f5f6fa")
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var, font=("Consolas", 22), bd=0, bg="#f5f6fa", justify='right', relief='flat', state='readonly', readonlybackground="#f5f6fa")
        self.entry.pack(fill='both', expand=True)
    def set(self, value):
        self.var.set(value)
    def get(self):
        return self.var.get()
