starting_string = input()
modified_string = ""

while True:

    command = input()

    if command == "Done":
        break

    splitted_command = command.split()
    real_command = splitted_command[0]

#---------------------------------------------------------

    if real_command == "Change":
        char = splitted_command[1]
        new_char = splitted_command[2]

        for element in starting_string:
            if element == char:
                modified_string += new_char
            else:
                modified_string += element

        starting_string = modified_string

        print(starting_string)
#---------------------------------------------------------

    elif real_command == "Includes":
        substring = splitted_command[1]

        if substring in starting_string:
            print("True")
        else:
            print("False")
#---------------------------------------------------------

    elif real_command == "End":
        substring = splitted_command[1]

        if starting_string.endswith(substring):
            print("True")
        else:
            print("False")
#--------------------------------------------------------

    elif real_command == "Uppercase":

        starting_string = starting_string.upper()
        print(starting_string)
#--------------------------------------------------------

    elif real_command == "FindIndex":
        char = splitted_command[1]

        print(starting_string.index(char))
#-------------------------------------------------------

    elif real_command == "Cut":
        start_index = int(splitted_command[1])
        count = int(splitted_command[2])

        end_index = start_index + count - 1

        cut_part = starting_string[start_index:end_index + 1]
        starting_string = starting_string[:start_index] + starting_string[end_index + 1:]

        print(cut_part)


