max_messages_count = int(input())
users_dict = {}
while True:

    command = input().split("=")

    if command[0] == "Statistics":
        break

    real_command = command[0]

    if real_command == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])

        if username not in users_dict.keys():
            users_dict[username] = [sent, received]

#-------------------------------------------------------------

    elif real_command == "Message":
        sender = command[1]
        receiver = command[2]

        if sender in users_dict.keys() and receiver in users_dict.keys():

            users_dict[sender][0] += 1
            users_dict[receiver][1] += 1

            if users_dict[sender][0] >= 10:
                print(f"{sender} reached the capacity!")
                del users_dict[sender]
            if users_dict[receiver][1] >= 10:
                print(f"{receiver} reached the capacity!")
                del users_dict[receiver]
#---------------------------------------------------------------

    elif real_command == "Empty":
        username = command[1]

        if username == "All":
            users_dict.clear()

        if username in users_dict.keys():
            del users_dict[username]

#----------------------------------------------------------------

print(f"Users count: {len(users_dict)}")

for key, value in users_dict.items():
    total_messages = 0
    for el in value:
        total_messages += int(el)

    print(f"{key} - {total_messages}")


