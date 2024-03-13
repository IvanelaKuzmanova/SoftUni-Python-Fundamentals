students_dict = {}
language_submissions = {}

while True:

    command = input().split("-")

    if command[0] == "exam finished":
        break

    username = command[0]
    current_command = command[1]
    points = 0

    if len(command) > 2:
        language = command[1]
        points = int(command[2])

    if current_command != "banned":
        if username in students_dict.keys():
            if points > students_dict[username]:
                students_dict[username] = points
        else:
            students_dict[username] = points

    # if current_command != "banned":
    #     if username not in students_dict.keys():
    #         students_dict[username] = {}
    #         if language not in students_dict[username].keys():
    #             students_dict[username]["language"] = language
    #             students_dict[username]["points"] = points
    #         else:
    #             if points > students_dict[username]["points"]:
    #                 students_dict[username]["points"] = points
#--------------------------------------------------------------------------------

        if language not in language_submissions.keys():
            language_submissions[language] = 0
        language_submissions[language] += 1

    else:
        students_dict.pop(username)
#--------------------------------------------------------------------------------

print("Results:")
for user, result in students_dict.items():
    print(f"{user} | {result}")

print("Submissions:")
for language, count in language_submissions.items():
    print(f"{language} - {count}")