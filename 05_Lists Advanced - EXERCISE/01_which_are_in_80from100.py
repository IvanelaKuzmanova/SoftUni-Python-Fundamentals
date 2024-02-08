def checking_string_parts(list_1:list, list_2:list) -> list:

    new_list = []

    for element in list_one:        #to take each object from list one
        for word in list_two:       #to iterate each object fro list two with each element from list one
            if element in word:
                new_list.append(element)      #to append elements found in the list only once (and skip if already added)
                break

    return new_list


list_one = input().split(', ')
list_two = input().split(', ')

checking = checking_string_parts(list_one, list_two)
print(checking)

