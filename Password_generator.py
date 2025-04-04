import random

# Custom character sets
LOWER = 'abcdefghjkmnpqrstuvwxyz'
UPPER = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
DIGITS = '23456789'
SYMBOLS = '@#%&*!?'

def custom_password_generator(length, complexity):
    char_pool = ''
    if complexity == 1:
        char_pool = LOWER + DIGITS
    elif complexity == 2:
        char_pool = LOWER + UPPER + DIGITS
    elif complexity >= 3:
        char_pool = LOWER + UPPER + DIGITS + SYMBOLS

    if not char_pool:
        raise ValueError("Invalid complexity level.")

    # Ensure password includes at least one character from each required set
    password = []
    if complexity >= 1:
        password.append(random.choice(LOWER))
        password.append(random.choice(DIGITS))
    if complexity >= 2:
        password.append(random.choice(UPPER))
    if complexity >= 3:
        password.append(random.choice(SYMBOLS))

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle to avoid predictable structure
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=== Custom Password Generator ===")
    try:
        length = int(input("Enter password length (min 4): "))
        complexity = int(input("Enter complexity level (1: Basic, 2: Medium, 3: Strong): "))

        if length < 4:
            print("Password length should be at least 4.")
            return
        if complexity not in [1, 2, 3]:
            print("Complexity must be 1, 2, or 3.")
            return

        password = custom_password_generator(length, complexity)
        print(f"Your generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
