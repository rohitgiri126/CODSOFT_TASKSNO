import random
import string


def generate_password():
    while True:
        print("\n==============================")
        print("      PASSWORD GENERATOR")
        print("==============================")

        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
                continue

            characters = (
                string.ascii_letters
                + string.digits
                + string.punctuation
            )

            password = "".join(random.choice(characters) for _ in range(length))

            print("\nGenerated Password:")
            print(password)

            again = input(
                "\nDo you want to generate another password? (yes/no): "
            ).lower()

            if again != "yes":
                print("Thank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    generate_password()