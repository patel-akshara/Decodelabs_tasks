import random
import string

length = int(input("Enter password length (minimum 3): "))

if length < 3:
    print("Password length must be at least 3.")
else:
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)
    ]

    remaining = length - 3
    all_chars = string.ascii_letters + string.digits

    for _ in range(remaining):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    final_password = ''.join(password)

    print("Generated Password:", final_password)
