def password_verification(current_object):

    digits_counter = 0
    valid = True

    if not 6 <= len(current_object) <= 10:
        valid = False
        print(f"Password must be between 6 and 10 characters")

    for symbol in range(len(current_object)):
        current_symbol = current_object[symbol]

        if current_symbol.isdigit():
            digits_counter += 1
            continue
        if not current_symbol.isalpha() and not current_symbol.isdigit():
            valid = False
            print(f"Password must consist only of letters and digits")
            break

    if digits_counter < 2:
        valid = False
        print(f"Password must have at least 2 digits")

    if valid:
        print(f"Password is valid")

password = input()

check_result = password_verification(password)