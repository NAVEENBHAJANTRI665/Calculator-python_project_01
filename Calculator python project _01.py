# ==========================================
#          PYTHON CALCULATOR PROJECT
# ==========================================

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


def modulus(a, b):
    if b == 0:
        return "Error: Cannot find modulus with zero"
    return a % b


def power(a, b):
    return a ** b


def floor_division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b


def calculator():
    while True:
        print("\n" + "=" * 45)
        print("          PYTHON CALCULATOR")
        print("=" * 45)

        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Floor Division (//)")
        print("8. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-8): ")

        # Exit
        if choice == "8":
            print("\nThank you for using the calculator!")
            break

        # Check valid choice
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice! Please select 1-8.")
            continue

        # Get numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform calculation
        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operator = "/"

        elif choice == "5":
            result = modulus(num1, num2)
            operator = "%"

        elif choice == "6":
            result = power(num1, num2)
            operator = "**"

        elif choice == "7":
            result = floor_division(num1, num2)
            operator = "//"

        # Display result
        print("\n" + "-" * 45)
        print(f"Calculation: {num1} {operator} {num2}")
        print(f"Result: {result}")
        print("-" * 45)


# Start calculator
calculator()