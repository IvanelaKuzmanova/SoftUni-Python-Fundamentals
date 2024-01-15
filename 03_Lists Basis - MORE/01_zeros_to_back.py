elements = input().split(", ")

rearranged_list = []
zeroes_counter = 0

for number in elements:

    if number != "0":
        rearranged_list.append(number)
    elif number == "0":
        zeroes_counter += 1

for zeroes in range(zeroes_counter):
    rearranged_list.append("0")

print([int(x) for x in rearranged_list])        #list comprehension using for cycle to convert all elements from the list


