coffee_list = input().split()
commands_count = int(input())

for element in range(commands_count):

    current_command = input().split()
    command_type = current_command[0]

    if command_type == "Include":
        coffee_list.append(current_command[1])

    elif command_type == "Remove":
        additional_command = current_command[1]
        number_of_coffees = int(current_command[2])

        if number_of_coffees > len(coffee_list):
            continue

        if additional_command == "first":
            coffee_list = coffee_list[number_of_coffees:]
        elif additional_command == "last":
            coffee_list = coffee_list[:len(coffee_list) - number_of_coffees]

    elif command_type == "Prefer":
        index_one = int(current_command[1])
        index_two = int(current_command[2])

        if index_one <= len(coffee_list) - 1 and index_two <= len(coffee_list) - 1:
            coffee_list[index_one], coffee_list[index_two] = coffee_list[index_two], coffee_list[index_one]
        else:
            continue

    elif command_type == "Reverse":
        coffee_list.reverse()

print("Coffees:")
print(" ".join(coffee_list))


