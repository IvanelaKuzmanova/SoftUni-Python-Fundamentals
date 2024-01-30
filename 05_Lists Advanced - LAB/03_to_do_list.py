command = input()

commands_list = []

while command != "End":

    commands_list.append(command)
    command = input()

sorted_list = sorted(commands_list, key=lambda current_command: int(current_command.split("-")[0]))     #splitting each command to number and task, splitting the dashes and sorting all elements in the list by the element on the zero index in current command

final_list = [command.split("-")[1] for command in sorted_list]     #adds all elements on index 1, ignoring dashes, to a new list

print(final_list)


