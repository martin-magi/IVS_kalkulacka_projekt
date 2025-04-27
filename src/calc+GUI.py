import tkinter as tk
from tkinter import ttk
import os
import calculator


def button_click(value):
    output_entry.config(fg="black", readonlybackground="white")
    current = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, current + str(value))


def clear_display():
    input_entry.delete(0, tk.END)
    output_var.set("")
    output_entry.config(fg="black", readonlybackground="white")


def backspace():
    current = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, current[:-1])


def calculate_result(event=None):
    try:
        expr = input_entry.get().strip()
        expr = expr.replace("^", "**")

        if expr.startswith("sin(") and expr.endswith(")"):
            num = float(expr[4:-1])
            result = calculator.sin(num)
        elif expr.startswith("fact(") and expr.endswith(")"):
            num = float(expr[5:-1])
            result = calculator.factorial(int(num))
        elif expr.startswith("√(") and expr.endswith(")"):
            num = float(expr[2:-1])
            result = calculator.root(num, 2)
        elif "^2" in expr:
            base = float(expr.replace("^2", ""))
            result = calculator.power(base, 2)
        elif "%" in expr:
            parts = expr.split("%")
            if len(parts) != 2:
                raise ValueError("Zlý zápis pre modulo. Skús napr. 6%5")
            a, b = float(parts[0]), float(parts[1])
            result = calculator.modulo(a, b)
        else:
            result = eval(expr)

        output_var.set(str(result))
        output_entry.config(fg="black", readonlybackground="white")
    except Exception as e:
        output_var.set(f"Chyba: {str(e)}")
        output_entry.config(fg="red", readonlybackground="#ffe6e6")


def show_info_window():
    info_win = tk.Toplevel(root)
    info_win.title("O aplikácii")
    info_win.resizable(False, False)
    info_win.iconbitmap(icon_path)
    info_text = """
IVS Kalkulačka – Popis funkcionality:

Táto kalkulačka podporuje:
- Základné operácie: +, -, *, / (napr. 2+2)
- Mocniny cez ^ (napr. 2^3)
- Druhá mocnina cez tlačidlo x²
- Odmocnina cez √(číslo)
- Modulo cez % (napr. 10%3)
- Sinus cez sin(uhol v stupňoch)
- Faktoriál cez ! (napr. 5!)
- Enter funguje ako rovná sa
- Klávesa 'c' funguje ako Clear
"""
    label = tk.Label(info_win, text=info_text, justify="left", padx=20, pady=20, font=("Helvetica", 12))
    label.pack()


# === Hlavné okno ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, "data", "icon.ico")

root = tk.Tk()
root.title("IVS Kalkulačka")
root.configure(bg="#b0b0b0")
root.resizable(False, False)
root.iconbitmap(icon_path)

# Klávesy
root.bind("<Return>", calculate_result)
root.bind("<c>", lambda event: clear_display())
root.bind("<C>", lambda event: clear_display())

# === Štýly ===
style = ttk.Style()
style.theme_use("clam")

style.configure("Calc.TButton", font=("Helvetica", 13, "bold"), padding=8)
style.configure("Equal.TButton", font=("Helvetica", 13, "bold"), background="#4CAF50",
                foreground="white", padding=8)
style.map("Equal.TButton", background=[("active", "#45a049")])

style.configure("Info.TButton", font=("Helvetica", 13, "bold"), background="#2196F3",
                foreground="white", padding=8)
style.map("Info.TButton", background=[("active", "#1e88e5")])

# === Výstupný rám ===
output_frame = tk.Frame(root, bg="#b0b0b0")
output_frame.pack(padx=8, pady=(8, 2), fill="x")

output_var = tk.StringVar()
output_entry = tk.Entry(output_frame, font=("Helvetica", 30), bd=0, relief="flat",
                        justify="right", state="readonly", textvariable=output_var,
                        readonlybackground="white", fg="black")
output_entry.pack(fill="x", expand=True, ipady=18)

# Oddelovací pásik
separator = tk.Frame(root, bg="#999999", height=2)
separator.pack(fill="x", padx=10, pady=(0, 6))

# === Vstupný rám ===
input_frame = tk.Frame(root, bg="#b0b0b0")
input_frame.pack(padx=8, pady=(0, 8), fill="x")

input_entry = tk.Entry(input_frame, font=("Helvetica", 24), bd=0, relief="flat",
                       justify="right", fg="black")
input_entry.pack(fill="x", expand=True, ipady=12)

# === Tlačidlá ===
button_frame = tk.Frame(root, bg="#b0b0b0")
button_frame.pack(padx=8, pady=8)

buttons = [
    ["7", "8", "9", "÷", "←", "C", "i"],
    ["4", "5", "6", "×", "(", ")"],
    ["1", "2", "3", "−", "x²", "√"],
    ["0", ".", "%", "+", "sin", "!", "="],
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if not char:
            continue

        if char == "←":
            cmd = backspace
        elif char == "C":
            cmd = clear_display
        elif char == "=":
            cmd = calculate_result
        elif char == "x²":
            cmd = lambda: button_click("^2")
        elif char == "√":
            cmd = lambda: button_click("√(")
        elif char == "÷":
            cmd = lambda: button_click("/")
        elif char == "×":
            cmd = lambda: button_click("*")
        elif char == "−":
            cmd = lambda: button_click("-")
        elif char == "sin":
            cmd = lambda: button_click("sin(")
        elif char == "i":
            cmd = show_info_window
        elif char == "%":
            cmd = lambda: button_click("%")
        elif char == "!":
            cmd = lambda: button_click("fact(") 
        else:
            cmd = lambda val=char: button_click(val)

        btn_style = "Calc.TButton"
        if char == "=":
            btn_style = "Equal.TButton"
        elif char == "i":
            btn_style = "Info.TButton"

        ttk.Button(button_frame, text=char, command=cmd, style=btn_style, width=6).grid(
            row=r, column=c, padx=4, pady=4, sticky="nsew"
        )

for i in range(7):
    button_frame.columnconfigure(i, minsize=60)

root.mainloop()
