light_side = {}
dark_side = {}

while True:

    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        splitted_command = command.split(" | ")
        side = splitted_command[0]
        user = splitted_command[1]

        if side == "Light":
            if side not in light_side.keys():
                light_side[side] = []
            if user not in light_side[side] and user not in dark_side[side]:
                light_side[side].append(user)

        elif side == "Dark":
            if side not in dark_side.keys():
                dark_side[side] = []
            if user not in dark_side[side]:
                dark_side[side].append(user)


    elif "->" in command:
        splitted_command = command.split(" -> ")
        user = splitted_command[0]
        side = splitted_command[1]

print(dark_side)
print(light_side)
