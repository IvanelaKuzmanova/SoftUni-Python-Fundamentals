# # string = input()
# # unique_chars = []
# #
# # for index in range(len(string) - 1, 0, -1):
# #
# #     if string[index] != string[index + 1]:
# #         unique_chars.append(string[index])
# #
# # new_string = "".join(unique_chars)
# # print(new_string)
#
#
# string = input()
# string_list = list(string)
#
# for index in range(len(string) - 1, 0, -1):
#     if string[index] == string[index - 1]:
#         string_list.pop(index)
#
# print(*string_list, sep="")


#solution 2:

text = input()
final_text = ""
last_added_char = ""

for char in text:
    if char != last_added_char:
        final_text += char
        last_added_char = char

print(final_text)