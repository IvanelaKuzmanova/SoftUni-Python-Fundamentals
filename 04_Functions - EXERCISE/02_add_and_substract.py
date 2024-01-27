def sum_numbers(num1, num2) -> int:
    return num1 + num2


def substract(new_num, num3) -> int:
    return new_num - num3


def add_and_substract(num1, num2, num3) -> int:            #added function which calls the other two (as required in the task)
    sum_of_first_two = sum_numbers(num1, num2)
    final_result = substract(sum_of_first_two, num3)
    return final_result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_substract(number_1, number_2, number_3))