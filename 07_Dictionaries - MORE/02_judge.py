contests_dict = {}

user_totalpoints_dict = {}

while True:
    command = input()

    if command == "no more time":
        break

    splitted_command = command.split(" -> ")

    username = splitted_command[0]
    contest = splitted_command[1]
    points = int(splitted_command[2])

    if username not in user_totalpoints_dict.keys():
        user_totalpoints_dict[username] = 0

    if contest not in contests_dict.keys():
        contests_dict[contest] = {}

    if username not in contests_dict[contest]:
        contests_dict[contest][username] = points
        user_totalpoints_dict[username] += points
    else:
        if contests_dict[contest][username] < points:
            user_totalpoints_dict[username] += points - contests_dict[contest][username]
            contests_dict[contest][username] = points

#--------------------------------------------------------------------------

for contest, participants in contests_dict.items():
    print(f"{contest}: {len(participants)} participants")

    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    place = 0
    for person, score in sorted_participants:
        place += 1
        print(f"{place}. {person} <::> {score}")

print("Individual standings:")
sorted_totalpoints = sorted(user_totalpoints_dict.items(), key=lambda x: (-x[1], x[0]))
place = 0
for name, pts in sorted_totalpoints:
    place += 1
    print(f"{place}. {name} -> {pts}")