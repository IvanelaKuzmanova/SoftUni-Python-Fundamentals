while True:

    command = input()

    if command == "end":
        break

    reversed_command = command[::-1]

    print(f"{command} = {reversed_command}")