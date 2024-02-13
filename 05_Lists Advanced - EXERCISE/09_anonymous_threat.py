my_list = input().split()

while True:
    first_command = input()

    if first_command == "3:1":
        break

    command = first_command.split()
    current_command = command[0]


    if current_command == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:                 #checking if the given index is existing in the list
            start_index = 0
        elif start_index > len(my_list) - 1:
            start_index = len(my_list) - 1
        if end_index > len(my_list) - 1:
            end_index = len(my_list) - 1
        elif end_index < 0:
            end_index = 0

        if start_index >= end_index:
            continue

        merged_text = ''.join(my_list[start_index:end_index + 1])       #combining everything from the list between the given indices (end + 1 to be included)
        my_list[start_index:end_index + 1] = [merged_text]        #modifying the list to take merged text on places of indices from the given range (merged_text is a list, sinc we need it to be treated as one element, not as strings

    elif current_command == 'divide':
        index = int(command[1])
        partition = int(command[2])

        modified_element = my_list[index]
        divided_elements = []

        partitions_length = len(modified_element) // partition       #how long should each partition be (except the last one, which could be longer)

        for current_element_index in range(partition - 1):          #for all partitions except the last one

            divided_elements.append(modified_element[:partitions_length])       #adding element with defined lengths to the new list
            modified_element = modified_element[partitions_length:]             #excluding added to list partition from the modified element

        divided_elements.append(modified_element)           #adding the rest left from the element to the list

        my_list[index:index + 1] = divided_elements       #replacing element on the given indice with the new patitions from the new list


print(' '.join(my_list))