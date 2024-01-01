word = input()

word_letters = list(word)


for i in word_letters:

    if str(i).isupper():

        print(word_letters.index(i), end=" ")



#
# for i in range(len(word)):
#
#