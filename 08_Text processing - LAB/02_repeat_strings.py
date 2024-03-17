strings_list = input().split()
repeated_strings = [word * len(word) for word in strings_list]

# for word in strings_list:
#
#     new_word = word * len(word)
#     repeated_strings.append(new_word)

print("".join(repeated_strings))
