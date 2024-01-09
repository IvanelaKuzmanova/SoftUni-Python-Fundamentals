string = input()

my_list = string.split()
opposite_list = []

for number in my_list:

    new_number = -int(number)

    opposite_list.append(new_number)

print(opposite_list)

