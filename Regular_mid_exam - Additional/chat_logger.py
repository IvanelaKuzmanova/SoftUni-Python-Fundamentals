command = input()
chat_history = []

while command != "end":

    splitted_command = command.split()
    actual_command = splitted_command[0]

    if actual_command == "Chat":
        message = splitted_command[1]
        chat_history.append(message)

    elif actual_command == "Delete":
        message = splitted_command[1]
        chat_history = [x for x in chat_history if x != message]

    elif actual_command == "Edit":
        message = splitted_command[1]
        new_message = splitted_command[2]
        for index in range(len(chat_history)):
            if chat_history[index] == message:
                chat_history[index] = new_message

    elif actual_command == "Pin":
        message = splitted_command[1]
        for index in range(len(chat_history)):
            if chat_history[index] == message:
                pinned_message = chat_history[index]
                chat_history.remove(pinned_message)
                chat_history.append(pinned_message)

    elif actual_command == "Spam":
        messages_list = splitted_command[1:]
        chat_history += messages_list

    command = input()

for item in chat_history:
    print(item)



