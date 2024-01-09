number = int(input())

numbers_list = []
filtered_list = []

for _ in range(number):
    current_number = int(input())
    numbers_list.append(current_number)

command = input()

if command == "even":
    for element in numbers_list:
        if element % 2 == 0 or element == 0:
            filtered_list.append(element)
elif command == "odd":
    for element in numbers_list:
        if element % 2 != 0:
            filtered_list.append(element)
elif command == "negative":
    for element in numbers_list:
        if element < 0:
            filtered_list.append(element)
elif command == "positive":
    for element in numbers_list:
        if element >= 0:
            filtered_list.append(element)

print(filtered_list)

