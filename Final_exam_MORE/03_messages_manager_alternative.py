capacity = int(input())
text = input().split("=")
messages_dict = {}

while text[0] != "Statistics":

    command = text[0]

    if command == "Add":
        username = text[1]
        sent = int(text[2])
        received = int(text[3])
        if username not in messages_dict.keys():
            messages_dict[username] = [sent, received]

    elif command == "Message":
        sender = text[1]
        receiver = text[2]
        if sender in messages_dict.keys() and receiver in messages_dict.keys():
            messages_dict[sender][0] += 1
            messages_dict[receiver][1] += 1
            if (messages_dict[sender][0] + messages_dict[sender][1]) >= capacity:
                print(f"{sender} reached the capacity!")
                del messages_dict[sender]
            if (messages_dict[receiver][1] + messages_dict[receiver][0]) >= capacity:
                print(f"{receiver} reached the capacity!")
                del messages_dict[receiver]

    elif command == "Empty":
        username = text[1]
        if username == "All":
            messages_dict.clear()
        if username in messages_dict.keys():
            del messages_dict[username]

    text = input().split("=")

print(f"Users count: {len(messages_dict)}")

for user, messages in messages_dict.items():
    total_messages = 0
    for el in messages:
        total_messages += int(el)
    print(f"{user} - {total_messages}")


