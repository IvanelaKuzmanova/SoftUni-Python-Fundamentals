# number = input()
#
# for digit in range(len(number)):
#
#     digit_to_print = number[digit]
#
#     l = list(str(digit_to_print))
#
#     print(max(digit_to_print), end="")


# for digit in range(len(number)):
#
#     print(max(l), end="")
#     list.remove(max(l))



number = input()

arranged = sorted(number, reverse=True)         #sorted function sorts strings from input (creates a list)

for i in arranged:              #using cycle to print needed symbols from the list as word, not in []
    if str(i).isdigit():            #isdigit - checks if each index of the list is digit
        print(i, end="")



