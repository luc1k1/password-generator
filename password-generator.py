import random
import string

def generate_password(length: int) -> str:
    """Generates a random password of the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def get_password_length() -> int:
    """Asks the user for the password length and ensures it's valid."""
    while True:
        try:
            length = int(input("Enter the number of characters for the password: "))
            if length > 0:
                return length
            print("Error: Please enter a number greater than 0.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def main():
    """Main function to generate and display the password."""
    length = get_password_length()
    print("Your generated password:", generate_password(length))

if __name__ == "__main__":
    main()
