items_list = []

while True:

    command = input()

    if command == "stop":
        break

    items_list.append(command)

items_dictionary = {}

for index in range(0, len(items_list), 2):

    key = items_list[index]
    value = items_list[index + 1]

    if key not in items_dictionary.keys():
        items_dictionary[key] = int(value)
    else:
        items_dictionary[key] += int(value)


for item, quantity in items_dictionary.items():
    print(f"{item} -> {quantity}")
