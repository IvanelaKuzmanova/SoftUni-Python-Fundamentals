phonebook = {}

while True:

    command = input()

    if "-" not in command:
        searches = int(command)
        break

    splitted_info = command.split("-")

    name = splitted_info[0]
    number = splitted_info[1]

    phonebook[name] = number

for search in range(searches):
    name_to_search = input()

    if name_to_search not in phonebook.keys():
        print(f"Contact {name_to_search} does not exist.")

    elif name_to_search in phonebook.keys():
            print(f"{name_to_search} -> {phonebook[name_to_search]}")



