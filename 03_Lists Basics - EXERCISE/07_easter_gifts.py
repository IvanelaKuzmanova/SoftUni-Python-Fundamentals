gifts_list = input().split()        #creating a list with gifts
command = input()

while not command == "No Money":
    command = command.split()   # separating elements from the command to a list, so  that they can me filtered
    command_from_index = command[0]
    gift_type = command[1]

    if command_from_index == "OutOfStock":
        for index in range(len(gifts_list)):
            if gifts_list[index] == gift_type:
                gifts_list[index] = "None"

    elif command_from_index == "Required":          #only in that case we will have 3rd index, e.g. [2]
        command_index = int(command[2])
        if command_index in range(len(gifts_list)):
            gifts_list[command_index] = gift_type

    elif command_from_index == "JustInCase":
        gifts_list.pop(-1)          #could just be pop() without -1
        gifts_list.append(gift_type)

    command = input()

for element in gifts_list:          #checking if any of the elements are "None" and removing them
    if element == "None":
        gifts_list.remove(element)

print(*gifts_list, sep=" ")         #printing with the described formatting and separation