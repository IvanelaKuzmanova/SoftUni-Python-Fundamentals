numbers_list = list(map(int, input().split(", ")))
even_index = []

for index in range(len(numbers_list)):

    if numbers_list[index] % 2 == 0:
        even_index.append(index)

print(even_index)

