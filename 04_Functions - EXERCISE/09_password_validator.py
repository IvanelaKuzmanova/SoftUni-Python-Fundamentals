current_object = input()
valid = True
digits_counter = 0
# def password_check(current_object):

if len(current_object) < 6:
    valid = False
    print(f"Password must be between 6 and 10 characters")

if 6 <= len(current_object) <= 10:

    for symbol in range(len(current_object)):

        current_symbol = current_object[symbol]

        if current_symbol.isdigit():
            digits_counter += 1
            continue
        elif current_object.isalpha():
            continue
        else:
            valid = False
            print(f"Password must consist only of letters and digits")
            break

    if digits_counter < 2:
        print(f"Password must have at least 2 digits")

if valid:
    print(f"Password is valid")



