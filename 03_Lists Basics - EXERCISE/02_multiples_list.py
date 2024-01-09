factor = int(input())
count = int(input())

numbers_list = []

for number in range(1, count + 1):

    number *= factor
    numbers_list.append(number)

print(numbers_list)
