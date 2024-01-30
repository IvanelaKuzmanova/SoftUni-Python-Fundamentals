command = input()

commands_list = []

while command != "End":

    commands_list.append(command)
    command = input()

sorted_list = sorted(commands_list, key=lambda x: int(x.split("-")[0]))     #sorting all elements in the list by the element on the zero index and ignoring all dashes

final_list = [command.split("-")[1] for command in sorted_list]     #adds all elements on index 1, ignoring dashes, to a new list

print(final_list)


