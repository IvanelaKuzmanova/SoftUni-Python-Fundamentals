string = input()
new_string = ""
command = input()

while command != "Done":

    separate_commands = command.split()
    actual_command = separate_commands[0]

    if actual_command == "Change":
        char = separate_commands[1]
        new_char = separate_commands[2]
        for element in string:
            if element == char:
                new_string += new_char
            else:
                new_string += element
        string = new_string
        print(string)

    elif actual_command == "Includes":
        substring = separate_commands[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif actual_command == "End":
        substring = separate_commands[1]
        if string.endswith(substring):
            print("True")
        else:
            print("False")

    elif actual_command == "Uppercase":
        string = string.upper()
        print(string)

    elif actual_command == "FindIndex":
        char = separate_commands[1]
        print(string.index(char))

    elif actual_command == "Cut":
        start = int(separate_commands[1])
        count = int(separate_commands[2])
        end = start + count - 1
        cut_string = string[start:end + 1]
        string = string[:start] + string[end + 1:]
        print(cut_string)

    command = input()