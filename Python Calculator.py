# This program acts as a simple python calculator which handles addition, subtraction, multiplication and division.

# Using a try-except block to handle cases where the user inputs non-numeric values.
try:
    # Ask the user for the first number and convert it to a float.
    num1 = float(input("Kindly enter the first number: "))
    # Ask the user for the second number and convert it to a float.
    num2 = float(input("Kindly enter the second number: "))
    # Ask the user for the desired operation.
    operator = input("Kindly enter a mathematical operator (+, -, *, /): ")

    # Using a variable to store the result, initialized to None.
    result = None

    # Check the operator and perform the calculation.
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Exception: Handle division by zero to prevent an error.
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero (Undefined function).")
            # Exit the program if a division by zero occurs.
            exit()
    else:
        # If the operator is not recognized, print an error message.
        print("Error: Invalid operator. Kindly use +, -, *, or /.")
        # Exit the program.
        exit()

    # If the calculation was successful, print the result in the requested format.
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    # Catch the error if the user enters something that isn't a number.
    print("Error: Invalid input. Kindly enter valid numbers.")
