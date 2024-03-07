words_list = input().split()

words_dict = {}

for word in words_list:
    word_lower = word.lower()       #turning all contents to lowercase since it is case insensitive!!

    if word_lower not in words_dict:
        words_dict[word_lower] = 0          #if not existing, adding as a key with value 0
    words_dict[word_lower] += 1         #adding 1 to the total count of the same word in the dictionary

for key, value in words_dict.items():
    if value % 2 != 0:          #checking if value is odd
        print(key, end = " ")           #printing the key corresponding to that value on the same row separated by space