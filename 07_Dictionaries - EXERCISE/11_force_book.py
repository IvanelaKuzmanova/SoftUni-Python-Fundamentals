sides_dict = {}
unique_users = []


while True:

    command = input()

    if command == "Lumpawaroo":
        break

    splitted_command = command.split(" | ")

    if len(splitted_command) > 1:           #if it is splitted
        side = splitted_command[0]
        user = splitted_command[1]
        if user not in unique_users:
            if side not in sides_dict:
                sides_dict[side] = []
            if user not in sides_dict[side]:
                sides_dict[side].append(user)
                unique_users.append(user)


    elif len(splitted_command) == 1:
        splitted_command_by_arrow = command.split(" -> ")
        user = splitted_command_by_arrow[0]
        side = splitted_command_by_arrow[1]

        if side not in sides_dict:
            sides_dict[side] = []
        for current_side, users in sides_dict.items():
            if user in users:
                sides_dict[current_side].remove(user)
        sides_dict[side].append(user)
        print(f"{user} joins the {side} side!")


for side, members in sides_dict.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for mem in members:
            print(f"! {mem}")