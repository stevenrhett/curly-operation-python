def val_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_symbols = False
    errors = []

    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_digit = True
        if not char.isalnum():
            has_symbols = True

    if not has_uppercase:
        errors.append("an uppercase letter")
    if not has_lowercase:
        errors.append("a lowercase letter")
    if not has_digit:
        errors.append("a digit")
    if not has_symbols:
        errors.append("a symbol character")

    if errors:
        print("Invalid password. Missing:", ", ".join(errors))
    else:
        print("Valid password!")


password = input("please enter your password: ")
val_password(password)
