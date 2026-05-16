
"""
Secure Password Generator
Creates a password with:
- Minimum length of 8
- Optional uppercase letters
- Optional lowercase letters
- Optional digits
- Optional special characters
"""

import random
import string

# Character pools
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = "!@#$%^&*()-_=+[]{};:,.<>?/"

MIN_LENGTH = 8


def get_yes_or_no(prompt: str) -> bool:
    """Ask the user a yes or no question."""

    while True:
        answer = input(prompt).strip().lower()

        if answer in ("yes", "y"):
            return True

        elif answer in ("no", "n"):
            return False

        else:
            print("Please enter yes or no.")


def get_password_length() -> int:
    """Get a valid password length from the user."""

    while True:
        try:
            length = int(input("How long do you want the password? "))

            if length >= MIN_LENGTH:
                return length
            else:
                print(f"Please enter a length of at least {MIN_LENGTH}.")

        except ValueError:
            print("Please enter a valid number.")


def get_criteria() -> dict:
    """Get password requirements from the user."""

    criteria = {
        "length": get_password_length(),
        "uppercase": get_yes_or_no("Do you want uppercase letters? "),
        "lowercase": get_yes_or_no("Do you want lowercase letters? "),
        "digits": get_yes_or_no("Do you want digits? "),
        "special": get_yes_or_no("Do you want special characters? ")
    }

    # Validation
    if not any([
        criteria["uppercase"],
        criteria["lowercase"],
        criteria["digits"],
        criteria["special"]
    ]):
        print("You must select at least one character type.")
        return get_criteria()

    return criteria


def build_pool(criteria: dict) -> tuple[str, list]:
    """Build the character pool and required characters."""

    pool = ""
    required = []

    if criteria["uppercase"]:
        pool += UPPERCASE
        required.append(random.choice(UPPERCASE))

    if criteria["lowercase"]:
        pool += LOWERCASE
        required.append(random.choice(LOWERCASE))

    if criteria["digits"]:
        pool += DIGITS
        required.append(random.choice(DIGITS))

    if criteria["special"]:
        pool += SPECIAL
        required.append(random.choice(SPECIAL))

    return pool, required


def generate_password(criteria: dict) -> str:
    """Generate a password based on the selected criteria."""

    pool, required = build_pool(criteria)

    length = criteria["length"]

    remaining_count = length - len(required)

    remaining = [
        random.choice(pool)
        for _ in range(remaining_count)
    ]

    password_chars = required + remaining

    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    """Main program loop."""

    while True:
        criteria = get_criteria()

        password = generate_password(criteria)

        print(f"\nGenerated Password: {password}\n")

        if not get_yes_or_no("Generate another password? "):
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()