import tkinter as tk
from logic.calculator import Calculator

class ButtonPanel(tk.Frame):
    def __init__(self, master, display, calculator):
        super().__init__(master, bg="#f5f6fa")
        self.display = display
        self.calculator = calculator
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]
        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(self, text=char, font=("Consolas", 18), width=4, height=2, bd=0, bg="#dff9fb", fg="#130f40", activebackground="#c7ecee", relief='flat', command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=r, column=c, padx=4, pady=4, sticky='nsew')
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
    def on_button_click(self, char):
        if char == 'C':
            self.display.set('')
            self.calculator.clear()
        elif char == '=':
            expr = self.display.get()
            try:
                result = self.calculator.evaluate(expr)
                self.display.set(result)
            except Exception:
                self.display.set('错误')
        else:
            self.display.set(self.display.get() + char)
