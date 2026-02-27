import tkinter as tk
import math

# -------------------- Main Window --------------------

root = tk.Tk()
root.title("Smart Pro Calculator")
root.geometry("500x650")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""

# -------------------- Functions --------------------


def update_expression(value):
    global expression
    expression += str(value)
    screen_var.set(expression)


def clear():
    global expression
    expression = ""
    screen_var.set("")


def backspace():
    global expression
    expression = expression[:-1]
    screen_var.set(expression)


def calculate():
    global expression
    try:
        result = eval(expression)
        history_box.insert(tk.END, f"{expression} = {result}\n")
        screen_var.set(result)
        expression = str(result)
    except:
        screen_var.set("Error")
        expression = ""


def scientific(func):
    global expression
    try:
        value = float(expression)

        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "square":
            result = value ** 2
        elif func == "log":
            result = math.log10(value)

        history_box.insert(tk.END, f"{func}({value}) = {result}\n")
        screen_var.set(result)
        expression = str(result)
    except:
        screen_var.set("Error")
        expression = ""

# -------------------- Screen --------------------


screen_var = tk.StringVar()

screen = tk.Entry(root,
                  textvariable=screen_var,
                  font=("Arial", 24),
                  bg="#2d2d2d",
                  fg="white",
                  bd=10,
                  relief=tk.FLAT,
                  justify="right")
screen.pack(fill="both", padx=10, pady=15)

# -------------------- Button Frame --------------------

buttons_frame = tk.Frame(root, bg="#1e1e1e")
buttons_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame, bg="#1e1e1e")
    row_frame.pack()
    for btn in row:
        def action(x=btn): return calculate(
        ) if x == "=" else update_expression(x)
        tk.Button(row_frame,
                  text=btn,
                  width=6,
                  height=2,
                  font=("Arial", 16),
                  bg="#3c3f41",
                  fg="white",
                  activebackground="#505354",
                  command=action).pack(side="left", padx=5, pady=5)

# -------------------- Scientific Buttons --------------------
# -------------------- Scientific Buttons --------------------

sci_frame = tk.Frame(root, bg="#1e1e1e")
sci_frame.pack(pady=10)


def clear_history():
    history_box.delete("1.0", tk.END)


sci_buttons = [
    ("sin", lambda: scientific("sin")),
    ("cos", lambda: scientific("cos")),
    ("tan", lambda: scientific("tan")),
    ("√", lambda: scientific("sqrt")),
    ("x²", lambda: scientific("square")),
    ("log", lambda: scientific("log")),
]

control_buttons = [
    ("⌫", backspace),
    ("C", clear),
    ("CE", clear_history)
]

# First Row (Scientific)
row1 = tk.Frame(sci_frame, bg="#1e1e1e")
row1.pack()

for text, cmd in sci_buttons:
    tk.Button(row1,
              text=text,
              width=6,
              height=2,
              font=("Arial", 14),
              bg="#ff9500",
              fg="white",
              activebackground="#e08900",
              command=cmd).pack(side="left", padx=5, pady=5)

# Second Row (Controls)
row2 = tk.Frame(sci_frame, bg="#1e1e1e")
row2.pack()

for text, cmd in control_buttons:
    tk.Button(row2,
              text=text,
              width=8,
              height=2,
              font=("Arial", 14),
              bg="#d32f2f",
              fg="white",
              activebackground="#b71c1c",
              command=cmd).pack(side="left", padx=8, pady=5)

# -------------------- History Panel --------------------

history_label = tk.Label(root,
                         text="History",
                         bg="#1e1e1e",
                         fg="white",
                         font=("Arial", 14))
history_label.pack()

history_box = tk.Text(root,
                      height=7,
                      bg="#2d2d2d",
                      fg="white",
                      font=("Arial", 12))
history_box.pack(fill="both", padx=10, pady=5)

# -------------------- Keyboard Support --------------------


def key_input(event):
    if event.char in "0123456789+-*/.":
        update_expression(event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()


root.bind("<Key>", key_input)

# -------------------- Run App --------------------

root.mainloop()
