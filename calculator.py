import tkinter as tk
from tkinter import messagebox

# ---------------------- Functions ----------------------
def calculate(operation):
    """Perform arithmetic operations with error handling."""
    try:
        num1 = float(num1_var.get())
        num2 = float(num2_var.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Error"

        result_label.config(text=f"Result: {result}", fg="green")

    except ValueError:
        result_label.config(text="Error: Enter valid numbers!", fg="red")
    except ZeroDivisionError:
        result_label.config(text="Error: Division by zero!", fg="red")


def clear_fields():
    """Clear all input fields and result label."""
    num1_var.set("")
    num2_var.set("")
    result_label.config(text="Result: ", fg="white")
    num1_entry.focus()


def quit_app():
    """Exit the application with confirmation."""
    if messagebox.askyesno("Exit", "Do you really want to quit?"):
        root.destroy()


# ---------------------- UI Setup ----------------------
root = tk.Tk()
root.title("Modern Tkinter Calculator")
root.geometry("380x420")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # Dark theme

# Variables
num1_var = tk.StringVar()
num2_var = tk.StringVar()

operation_symbol = {
    "add": "+",
    "subtract": "-",
    "multiply": "×",
    "divide": "÷"
}

# ---------------------- Widgets ----------------------
title_label = tk.Label(root, text="Modern Tkinter Calculator", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#00ffcc")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

tk.Label(frame, text="First Number:", font=("Arial", 12), bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="e")
num1_entry = tk.Entry(frame, textvariable=num1_var, font=("Arial", 12), width=15)
num1_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Second Number:", font=("Arial", 12), bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="e")
num2_entry = tk.Entry(frame, textvariable=num2_var, font=("Arial", 12), width=15)
num2_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=15)

btn_style = {"font": ("Arial", 12, "bold"), "width": 10, "bg": "#00ffcc", "fg": "black", "bd": 0, "pady": 5}

tk.Button(button_frame, text="Add", command=lambda: calculate("add"), **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtract", command=lambda: calculate("subtract"), **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", command=lambda: calculate("multiply"), **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", command=lambda: calculate("divide"), **btn_style).grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Clear", command=clear_fields, font=("Arial", 12), bg="#ff9800", fg="white", width=12).pack(pady=5)
tk.Button(root, text="Quit", command=quit_app, font=("Arial", 12), bg="#f44336", fg="white", width=12).pack(pady=5)

result_label = tk.Label(root, text="Result:", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="white")
result_label.pack(pady=10)


root.mainloop()
