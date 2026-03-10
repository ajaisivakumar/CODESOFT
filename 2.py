def calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    print("Operations: +, -, *, /")
    operation = input("Enter your operation choice: ")

    if operation == '+':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operation choice.")

if __name__ == "__main__":
    calculator()