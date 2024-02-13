def sorting_into_tens(list_of_numbers:list) -> str:

    current_group = 10

    while list_of_numbers:          #while there are elements in the list

        current_group_filtered = [n for n in list_of_numbers if n <= current_group]     #creates new list with all numbers lower than the boundary
        print(f"Group of {current_group}'s: {current_group_filtered}")

        current_group += 10
        list_of_numbers = [n for n in list_of_numbers if n not in current_group_filtered]       #a comprehension filtering all elements in the new list and removing them from tha main one


numbers_list = [int(x) for x in input().split(', ')]
result = sorting_into_tens(numbers_list)

