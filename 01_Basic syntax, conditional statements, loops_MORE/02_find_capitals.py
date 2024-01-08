# word = input()
#
# word_letters = list(word)
# index_list = []
#
# for i in word_letters:
#
#     if str(i).isupper():
#
#         print(word_letters.index(i), end=" ")


word = input()
index_list = []

for i in range(len(word)):

    if word[i].isupper():
        index_list.append(i)

print(index_list)