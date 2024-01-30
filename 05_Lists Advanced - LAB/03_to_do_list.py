command = input()

commands_list = []

while command != "End":

    commands_list.append(command)
    command = input()

commands_list.sort()

final_list = [command.split("-")[1] for command in commands_list]     #adds all elements on index 1, ignoring dashes, to a new list

print(final_list)


