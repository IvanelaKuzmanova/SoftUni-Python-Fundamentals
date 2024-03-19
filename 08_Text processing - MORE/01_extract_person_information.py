pairs_count = int(input())

for info in range(pairs_count):

    current_name = ""
    current_age = ""
    command = input()

    for index in range(len(command)):
        if command[index] == "@":
            index_number_increase = 1
            while not command[index + index_number_increase] == "|":
                current_name += command[index + index_number_increase]
                index_number_increase += 1
        if command[index] == "#":
            index_increase = 1
            while not command[index + index_increase] == "*":
                current_age += command[index + index_increase]
                index_increase += 1
    print(f"{current_name} is {current_age} years old.")

    # string_list = input().split()
    # current_name = ""
    # current_age = ""
    #
    # for word in string_list:
    #     if "@" in word and "|" in word:
    #         current_name += word
    #     elif "#" in word and "*" in word:
    #         current_age += word
    #
    # for char in current_name:
    #
    # # for element in string_list:
    # #
    # #     if element.startswith("@") and element.endswith("|"):
    # #         current_name += element[1: len(element) - 1]
    # #     elif element.startswith("#") and element.endswith("*"):
    # #         current_age += element[1: len(element) - 1]

    # print(f"{current_name} is {current_age} years old.")