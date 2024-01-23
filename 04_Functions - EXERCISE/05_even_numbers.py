def even(num):
    return num % 2 == 0         #definind function to check if a number is even (returning true or false)

numbers_list = [int(number) for number in input().split()]      #using list comprehension to create a list of integers from given string

result = filter(even, numbers_list)         #using filter build in function - filter all even numbers in the given list

print(list(result))       #using list function to print the new list with filtered elements (otherwise nothing is printed)