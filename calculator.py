import math


def perform_calculation():
    first_input = input("Enter the first number: ")
    operator = input("Enter an operator (+, -, *, /): ").strip()
    second_input = input("Enter the second number: ")

    try:
        first_number = float(first_input)
        second_number = float(second_input)
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if not math.isfinite(first_number) or not math.isfinite(second_number):
        print("Error: Please enter valid numbers.")
        return

    if operator not in ("+", "-", "*", "/"):
        print("Error: Invalid operator. Use +, -, *, or /.")
        return

    if operator == "/" and second_number == 0:
        print("Error: Cannot divide by zero.")
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
    return f"{first_number} {operator} {second_number} = {result}"


def show_history(history):
    if not history:
        print("No calculations yet.")
        return

    for number, record in enumerate(history, start=1):
        print(f"{number}. {record}")


def main():
    history = []
    while True:
        print("1. Calculate")
        print("2. Show history")
        print("3. Exit")
        try:
            choice = input("Choose an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("Goodbye!")
            break

        if choice == "1":
            try:
                record = perform_calculation()
            except (EOFError, KeyboardInterrupt):
                print("Goodbye!")
                break
            if record is not None:
                history.append(record)
        elif choice == "2":
            show_history(history)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid option. Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
