letters_list = [x for x in input() if x != " "]

dictionary = {}

for letter in letters_list:

    if letter not in dictionary.keys():
        dictionary[letter] = 0
    dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")


#advanced method:
#
# from collections import Counter
#
# def count_letter(text):
#     text = "".join(text)
#     chars_dict = Counter(text)
#
#     return chars_dict
#
#
# text = input().split()
# characters_dictionary = count_letter(text)
#
# for k, v in characters_dictionary.items():
#     print(f"{k} -> {v}")