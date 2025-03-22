import tkinter as tk
from calculator_logic import calculator  # Import backend

def evaluate_expression():
    expression = entry_var.get().strip()

    if any(op in expression for op in "+-*/"):  # Check if operator is present
        for op in "+-*/":
            if op in expression:
                a, b = expression.split(op)
                result = calculator(a, op, b)
                entry_var.set(result)
                return
    entry_var.set("Invalid Input")

# Tkinter GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify='right')
entry.pack(fill='both', padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack()
    for char in row:
        if char == '=':
            action = evaluate_expression
        elif char == 'C':
            action = lambda: entry_var.set("")
        else:
            action = lambda val=char: entry_var.set(entry_var.get() + val)
        
        btn = tk.Button(button_row, text=char, font=("Arial", 16), command=action, width=5, height=2)
        btn.pack(side='left', padx=5, pady=5)

root.mainloop()
