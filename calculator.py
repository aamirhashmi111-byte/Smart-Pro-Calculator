import math


# ----------- Basic Operations -----------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"

    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)


def percentage(a, b):
    return (a / 100) * b


# ----------- Scientific Operations -----------

def sine(a):
    return math.sin(math.radians(a))


def cosine(a):
    return math.cos(math.radians(a))


def tangent(a):
    return math.tan(math.radians(a))


# ----------- History Functions -----------

def save_history(text):
    with open("history.txt", "a") as file:
        file.write(text + "\n")


def clear_history():
    with open("history.txt", "w") as file:
        file.write("")
    print("History cleared successfully!")


def show_history():
    try:
        with open("history.txt", "r") as file:
            content = file.read()
            if content == "":
                print("No history found.")
            else:
                print("\n===== Calculation History =====")
                print(content)
    except FileNotFoundError:
        print("No history file found.")


# ----------- Main Program -----------

while True:
    print("\n===== Smart Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Show History")
    print("9. Clear History")
    print("10. Exit")
    print("11. Sine")
    print("12. Cosine")
    print("13. Tangent")

    choice = input("Choose an option (1-13): ")

    if choice == "10":
        print("Exiting calculator...")
        break

    try:

        # ----------- History Options -----------
        if choice == "8":
            show_history()
            continue

        elif choice == "9":
            clear_history()
            continue

        # ----------- Two Number Operations -----------
        elif choice in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

        # ----------- Single Number Operation -----------
        elif choice == "6":
            a = float(input("Enter number: "))

        # ----------- Scientific -----------
        elif choice in ["11", "12", "13"]:
            a = float(input("Enter angle in degrees: "))

        else:
            print("Invalid choice!")
            continue

        # ----------- Calculation Section -----------

        if choice == "1":
            result = add(a, b)
            operation = f"{a} + {b} = {result}"

        elif choice == "2":
            result = subtract(a, b)
            operation = f"{a} - {b} = {result}"

        elif choice == "3":
            result = multiply(a, b)
            operation = f"{a} * {b} = {result}"

        elif choice == "4":
            result = divide(a, b)
            operation = f"{a} / {b} = {result}"

        elif choice == "5":
            result = power(a, b)
            operation = f"{a} ^ {b} = {result}"

        elif choice == "6":
            result = square_root(a)
            operation = f"√{a} = {result}"

        elif choice == "7":
            result = percentage(a, b)
            operation = f"{a}% of {b} = {result}"

        elif choice == "11":
            result = sine(a)
            operation = f"sin({a}) = {result}"

        elif choice == "12":
            result = cosine(a)
            operation = f"cos({a}) = {result}"

        elif choice == "13":
            result = tangent(a)
            operation = f"tan({a}) = {result}"

        print("Result:", result)
        save_history(operation)

    except ValueError:
        print("Error: Please enter valid numbers!")
