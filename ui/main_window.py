import tkinter as tk
from ui.button_panel import ButtonPanel
from ui.display import Display
from logic.calculator import Calculator

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("精致计算器")
        self.resizable(False, False)
        self.configure(bg="#f5f6fa")
        self.calculator = Calculator()
        self.display = Display(self)
        self.display.pack(padx=10, pady=10)
        self.button_panel = ButtonPanel(self, self.display, self.calculator)
        self.button_panel.pack(padx=10, pady=(0,10))

def run_calculator():
    app = MainWindow()
    app.mainloop()
