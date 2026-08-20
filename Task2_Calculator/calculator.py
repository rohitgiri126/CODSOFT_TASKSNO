def calculator():
    while True:
        print("\n========================")
        print("       CALCULATOR")
        print("========================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("Thank you for using the Calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                print(f"Result = {result}")

            elif choice == "2":
                result = num1 - num2
                print(f"Result = {result}")

            elif choice == "3":
                result = num1 * num2
                print(f"Result = {result}")

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue

                result = num1 / num2
                print(f"Result = {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using the Calculator!")
            break


if __name__ == "__main__":
    calculator()