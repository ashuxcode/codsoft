import math

def calculator():
    print("===================================")
    print("     WELCOME TO PYTHON CALCULATOR  ")
    print("===================================")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Modulus (%)")
        print("8. Percentage")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        # Exit condition
        if choice == '9':
            print("\nThank you for using the calculator. Goodbye!")
            break

        # Square root needs only one number
        if choice == '6':
            num = float(input("Enter a number: "))
            print(f"√{num} = {math.sqrt(num)}")

        else:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        print(f"{num1} / {num2} = {num1 / num2}")
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {pow(num1, num2)}")
                elif choice == '7':
                    print(f"{num1} % {num2} = {num1 % num2}")
                elif choice == '8':
                    print(f"{num1} is { (num1/num2)*100 }% of {num2}")
                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                print("⚠️ Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
