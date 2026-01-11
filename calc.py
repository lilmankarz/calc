import tkinter as tk
from tkinter import messagebox

class Calculator:
    def add(self, x, y):
        answer = x + y
        return answer
    def subtract(self, x, y,):
        answer = x - y
        return answer
    def divide(self, x, y):
        answer = x / y
        return answer
    def multiply(self, x, y):
        answer = x * y
        return answer
    
calc = Calculator()

class CalculatorUI:
    def __init__(self, root, calculator):
        self.calc = calculator
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        # Calculator state
        self.current = ""
        self.operator = None
        self.previous = None

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.RIDGE,
            width=15
        )
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for text, row, col in buttons:
            self.create_button(text, row, col)

        # Make clear button span
        self.root.grid_slaves(row=5, column=0)[0].grid(columnspan=4, sticky="nsew")

    def create_button(self, text, row, col):
        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda t=text: self.on_press(t)
        )
        btn.grid(row=row, column=col, sticky="nsew")

    # =====================
    # Core input handling
    # =====================
    def on_press(self, value):
        if value.isdigit() or value == ".":
            self.current += value
            self.update_display(self.current)

        elif value in "+-*/":
            self.set_operator(value)

        elif value == "=":
            self.calculate()

        elif value == "C":
            self.clear()

    def set_operator(self, op):
        if self.current == "":
            return
        self.previous = float(self.current)
        self.operator = op
        self.current = ""
        self.update_display("")

    def calculate(self):
        if self.operator is None or self.current == "":
            return

        x = self.previous
        y = float(self.current)

        try:
            if self.operator == "+":
                result = self.calc.add(x, y)
            elif self.operator == "-":
                result = self.calc.subtract(x, y)
            elif self.operator == "*":
                result = self.calc.multiply(x, y)
            elif self.operator == "/":
                result = self.calc.divide(x, y)

            self.update_display(result)
            self.current = str(result)
            self.operator = None
            self.previous = None

        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear()

    def clear(self):
        self.current = ""
        self.operator = None
        self.previous = None
        self.update_display("")

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorUI(root, calc)
    root.mainloop()

