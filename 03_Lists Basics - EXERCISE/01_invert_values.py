string = input()

my_list = string.split()
opposite_list = []

for number in my_list:

    number = float(number)
    new_number = int(number) * -1

    opposite_list.append(new_number)

print(opposite_list)

