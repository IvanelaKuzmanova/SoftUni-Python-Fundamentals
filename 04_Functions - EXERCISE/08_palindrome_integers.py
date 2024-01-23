numbers_list = input().split(", ")          #creating a list with strings to be able to iterate with slice notation

def palindrome_check(current_object):

    for element in current_object:
        print(element == element[::-1])         #using slice notation to reverse the element and return true or false

result = palindrome_check(numbers_list)         #calling the function