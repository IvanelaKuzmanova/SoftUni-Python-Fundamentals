numbers_list = input().split()
numbers_to_remove = int(input())

smallest_num = 0
list_as_int = []

for i in numbers_list:
    list_as_int.append(int(i))          #to create a list with integers, not strings

for n in range(numbers_to_remove):      # iterations equal to the numbers to remove variable

    smallest_num = min(list_as_int)     #build in function to find the min value from a list. There is also one for MAX value
    list_as_int.remove(smallest_num)

print(*list_as_int, sep=", ")           # * before the list defines printing without the brackets, sep defines the way of separating elements
