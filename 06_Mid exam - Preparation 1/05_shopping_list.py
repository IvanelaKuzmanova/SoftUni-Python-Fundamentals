def shopping_list_definition(my_list:list) -> str:

    while True:

        command = input()

        if command == "Go Shopping!":
            break

        else:
            splitted_command = command.split()
            type = splitted_command[0]
            product = splitted_command[-1]

            if type == "Urgent":
                my_list.count(product)
                if product == 0:
                    my_list.insert(0, product)

            elif type == "Unnecessary":
                my_list = [item for item in my_list if item != product]         #filters only different products

            elif type == "Correct":
                old_product = splitted_command[1]
                for index in range(len(my_list)):
                    current_product = my_list[index]
                    if current_product == old_product:
                        current_product = product

            elif type == "Rearrange":
                for index in range(len(my_list)):
                    if my_list[index] == product:
                        removed_element = my_list.pop(index)
                        my_list.append(removed_element)

        return ", ".join(my_list)


shopping_list = input().split("!")

result = shopping_list_definition(shopping_list)
print(result)



