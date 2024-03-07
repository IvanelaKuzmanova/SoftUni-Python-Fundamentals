letters_list = [x for x in input() if x != " "]

dictionary = {}

for letter in letters_list:

    if letter not in dictionary.keys():
        dictionary[letter] = 0
    dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
