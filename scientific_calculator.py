import math

def basic_calculator():
    while True:
        print("Scientific Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Trigonometric Functions")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Calculator exiting. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        print("Error: Cannot divide by zero")
                        continue  # Ask for input again
            except ValueError:
                print("Error: Invalid input. Please enter valid numbers.")
                continue  # Ask for input again

        elif choice == '5':
            try:
                num = float(input("Enter a number: "))
                if num >= 0:
                    result = math.sqrt(num)
                else:
                    print("Error: Invalid input for square root")
                    continue  # Ask for input again
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue  # Ask for input again

        elif choice == '6':
            trig_input = input("Enter the trigonometric function and angle (e.g., 'sin 34'): ")
            parts = trig_input.split()
            if len(parts) != 2:
                print("Error: Invalid input format. Please enter 'function angle'.")
                continue  # Ask for input again

            trig_function, angle_degrees = parts[0], parts[1]

            try:
                angle_degrees = float(angle_degrees)
                angle_radians = math.radians(angle_degrees)

                if trig_function == 'sin':
                    result = math.sin(angle_radians)
                elif trig_function == 'cos':
                    result = math.cos(angle_radians)
                elif trig_function == 'tan':
                    result = math.tan(angle_radians)
                else:
                    print("Error: Invalid trigonometric function. Please use 'sin', 'cos', or 'tan'.")
                    continue  # Ask for input again
            except ValueError:
                print("Error: Invalid input. Please enter a valid angle.")
                continue  # Ask for input again
        else:
            print("Error: Invalid choice. Please choose a valid option.")
            continue  # Ask for input again

        print("Result:", result)

if __name__ == "__main__":
    basic_calculator()
