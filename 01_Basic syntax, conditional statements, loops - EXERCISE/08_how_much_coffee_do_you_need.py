command = input()
coffees_needed = 0

while command != "END":

    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":          #проверява дали това е думата, като преобразува доректно в малки букви. без значение как е въведена

        if command.islower():         #проверяваме дали е въведена с малки букви
            coffees_needed += 1
        else:                         #if command.isupper()
            coffees_needed += 2

    command = input()

if coffees_needed > 5:
    print(f"You need extra sleep")
else:
    print(coffees_needed)


