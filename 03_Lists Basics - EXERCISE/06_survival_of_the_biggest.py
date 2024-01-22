numbers_list = input().split()
removed = int(input())

deleted_value = 0

for i in range(removed):

    deleted_value = min(numbers_list)
    numbers_list.remove(deleted_value)

print(numbers_list)
