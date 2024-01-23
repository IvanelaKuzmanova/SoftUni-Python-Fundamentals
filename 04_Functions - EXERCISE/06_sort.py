def ascending_sorting(current_object):
    return sorted(current_object)           #defining function which sorts elements in ascending order

numbers_list = [int(number) for number in input().split()]      #list comprehension to create list with integers

result = list(ascending_sorting(numbers_list))      #calling the function and creating a list with the outcome

print(result)        #printing the results as list

