players_dict = {}

while True:

    command = input()

    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split("->")
        skill = int(skill)

        if player not in players_dict.keys():
            players_dict[player] = {position: skill}

        else:
            for key, value in players_dict[player].items():
                if value < skill:
                    value = skill
                    key = position

    else:
        pass

print(players_dict)