text = input()
total_strength = 0
final_string = ""

for index in range(len(text)):
    #explosion(number)
    if total_strength > 0 and text[index] != ">":
        total_strength -= 1

    #symbol >
    elif text[index] == ">":
        final_string += ">"
        total_strength += int(text[index + 1])

    #letter
    else:
        final_string += text[index]

print(final_string)


# for index in range(len(text) - 1):
#
#     current_char = text[index]
#
#     if current_char == ">":
#         current_strength = int(text[index + 1])
#
#         if current_strength > 1:
#             total_strength += current_strength - 1
#
#         text = text.replace(text[index+1], "")
#
# print(text)
