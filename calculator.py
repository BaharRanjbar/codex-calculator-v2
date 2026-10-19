def main():
    first_input = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ").strip()
    second_input = input("Enter the second number: ")

    try:
        first_number = float(first_input)
        second_number = float(second_input)
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operator not in ("+", "-", "*", "/"):
        print("Error: Invalid operator. Use +, -, *, or /.")
        return

    if operator == "/" and second_number == 0:
        print("Division by zero is not allowed.")
        return

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    else:
        result = first_number / second_number

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
