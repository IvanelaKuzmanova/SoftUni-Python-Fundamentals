valid_contests = {}

while True:

    command = input()

    if command == "end of contests":
        break

    splitted_command = command.split(":")

    contest = splitted_command[0]
    contest_pass = splitted_command[1]

    if contest not in valid_contests.keys():
        valid_contests[contest] = contest_pass

#-------------------------------------------------------------------------------

contest_participants = {}

while True:

    command_user = input()

    if command_user == "end of submissions":
        break

    actual_info = command_user.split("=>")

    contest_name = actual_info[0]
    current_pass = actual_info[1]
    username = actual_info[2]
    user_points = int(actual_info[3])

    if contest_name in valid_contests.keys() and current_pass == valid_contests[contest_name]:

        if username not in contest_participants.keys():
            contest_participants[username] = {contest_name: user_points}
        else:
            if contest_name not in contest_participants[username].keys():
                contest_participants[username][contest_name] = user_points

            else:
                if contest_participants[username][contest_name] < user_points:
                    contest_participants[username][contest_name] = user_points

#---------------------------------------------------------------------------------

users_totalpoints = {}

for person, result in contest_participants.items():
    person_total_points = 0

    for value in result.values():
        person_total_points += value

    users_totalpoints[person] = person_total_points

#--------------------------------------------------------------------------------

max_value = 0
winner = 0
for user, total in users_totalpoints.items():

    current_value = total

    if current_value > max_value:
        max_value = current_value
        winner = user

print(f"Best candidate is {winner} with total {max_value} points.")
print("Ranking:")

sorted_by_name = sorted(contest_participants.items(), key=lambda x: x[0])

#----------------------------------------------------------------------------------

for key, value in sorted_by_name:
    print(f"{key}")

    sorted_submissions = sorted(value.items(), key=lambda x: (-x[1]))

    for k, v in sorted_submissions:
        print(f"#  {k} -> {v}")