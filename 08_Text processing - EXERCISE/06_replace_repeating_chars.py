# string = input()
# unique_chars = []
#
# for index in range(len(string) - 1, 0, -1):
#
#     if string[index] != string[index + 1]:
#         unique_chars.append(string[index])
#
# new_string = "".join(unique_chars)
# print(new_string)


string = input()
string_list = list(string)

for index in range(len(string) - 1, 0, -1):
    if string[index] == string[index - 1]:
        string_list.pop(index)

print(*string_list, sep="")


# for char in string:
#
#     if char not in unique_chars:
#         unique_chars.append(char)
#
# new_string = "".join(unique_chars)
#
# print(new_string)