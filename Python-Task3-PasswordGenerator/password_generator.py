
import secrets
import string

MIN_LENGTH = 4
MAX_LENGTH = 128

LOOKALIKE_CHARACTERS = "0Ol1I"


# Shared password-generation function for CLI and GUI
def generate_password(
    length,
    use_upper,
    use_lower,
    use_digits,
    use_symbols,
    exclude_lookalikes=False
):
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(
            f"Password length must be between "
            f"{MIN_LENGTH} and {MAX_LENGTH}."
        )

    pools = []

    if use_upper:
        pools.append(string.ascii_uppercase)

    if use_lower:
        pools.append(string.ascii_lowercase)

    if use_digits:
        pools.append(string.digits)

    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("Select at least one character type.")

    # Remove look-alike characters if requested
    if exclude_lookalikes:
        pools = [
            "".join(
                char for char in pool
                if char not in LOOKALIKE_CHARACTERS
            )
            for pool in pools
        ]

        if any(not pool for pool in pools):
            raise ValueError(
                "A selected character type has no available characters."
            )

    # Guarantee one character from every selected type
    password_characters = [
        secrets.choice(pool) for pool in pools
    ]

    # Combine all selected character pools
    all_characters = "".join(pools)

    # Fill the remaining password length
    for _ in range(length - len(password_characters)):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Securely shuffle characters before joining
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


# Read a valid password length
def get_length():
    while True:
        try:
            length = int(
                input("Enter password length (4-128): ")
            )

            if MIN_LENGTH <= length <= MAX_LENGTH:
                return length

            print("Error: Length must be between 4 and 128.")

        except ValueError:
            print("Error: Please enter a whole number.")


# Read a yes/no answer
def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer in ("y", "n"):
            return answer == "y"

        print("Please enter y or n.")


# CLI application
def main():
    print("=" * 42)
    print("       SECURE PASSWORD GENERATOR")
    print("=" * 42)

    while True:
        length = get_length()

        # Ensure at least one character type is selected
        while True:
            print("\nSelect character types:")

            use_upper = ask_yes_no(
                "Include uppercase letters (A-Z)? (y/n): "
            )
            use_lower = ask_yes_no(
                "Include lowercase letters (a-z)? (y/n): "
            )
            use_digits = ask_yes_no(
                "Include digits (0-9)? (y/n): "
            )
            use_symbols = ask_yes_no(
                "Include symbols (!@#...)? (y/n): "
            )

            if any((use_upper, use_lower, use_digits, use_symbols)):
                break

            print(
                "\nError: Select at least one character type. "
                "Please try again."
            )

        exclude_lookalikes = ask_yes_no(
            "Exclude look-alike characters (0, O, l, 1, I)? (y/n): "
        )

        try:
            password = generate_password(
                length,
                use_upper,
                use_lower,
                use_digits,
                use_symbols,
                exclude_lookalikes
            )

            print("\nGenerated Password:", password)
            print("Password Length:", len(password))

        except ValueError as error:
            print("Error:", error)

        if not ask_yes_no("\nGenerate another? (y/n): "):
            print("\nThank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()
