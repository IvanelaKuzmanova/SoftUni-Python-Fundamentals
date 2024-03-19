keys_list = [int(x) for x in input().split()]

while True:
    string = input()
    if string == "find":
        break

    encrypted_message = ""
    treasure_type = ""
    location = ""
    key_index = 0

    for index in range(len(string)):
        if key_index == len(keys_list):
            key_index = 0           #to start with all keys from the beginning
        encrypted_message += chr(ord(string[index]) - keys_list[key_index])
        key_index += 1

    start_index_type = encrypted_message.index("&")
    encrypted_message = encrypted_message[start_index_type + 1:]
    end_index_type = encrypted_message.index("&")
    treasure_type = encrypted_message[:end_index_type]
    start_index_location = encrypted_message.index("<")
    encrypted_message = encrypted_message[start_index_location + 1:]
    end_index_location = encrypted_message.index(">")
    location = encrypted_message[:end_index_location]
    print(f"Found {treasure_type} at {location}")