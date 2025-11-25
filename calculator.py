# -------------------------------
# Project 1: Simple Calculator
# -------------------------------

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Clear")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "6":
            print("Exiting calculator…")
            break

        if choice == "5":
            print("Calculator cleared.")
            continue

        if choice not in ["1","2","3","4"]:
            print("Invalid option!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            print("Invalid number input!")
            continue

        if choice == "1": print("Result:", add(a,b))
        elif choice == "2": print("Result:", subtract(a,b))
        elif choice == "3": print("Result:", multiply(a,b))
        elif choice == "4": print("Result:", divide(a,b))

calculator()
