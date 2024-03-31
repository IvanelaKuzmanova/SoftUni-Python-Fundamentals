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
            messages_dict[username] = {"sent": sent, "received": received}

    elif command == "Message":
        sender = text[1]
        receiver = text[2]
        if sender in messages_dict.keys() and receiver in messages_dict.keys():
            messages_dict[sender]["sent"] += 1
            messages_dict[receiver]["received"] += 1
            if (messages_dict[sender]["sent"] + messages_dict[sender]["received"]) >= capacity:
                print(f"{sender} reached the capacity!")
                del messages_dict[sender]
            if (messages_dict[receiver]["received"] + messages_dict[receiver]["sent"]) >= capacity:
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
    for value in messages.values():
        total_messages = sum(messages.values())
    print(f"{user} - {total_messages}")


