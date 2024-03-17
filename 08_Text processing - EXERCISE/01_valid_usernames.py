def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False

def valid_chars(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True

def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def final_valid_check(name):
    if valid_length(name) and valid_chars(name) and no_redundant_symbols(name):
        return True
    return False


usernames_list = input().split(", ")

for username in usernames_list:
    if final_valid_check(username):
        print(username)