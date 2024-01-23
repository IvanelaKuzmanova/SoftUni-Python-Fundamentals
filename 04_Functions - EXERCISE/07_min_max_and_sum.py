# -------------solution 1 - if we should use functions separately and be able not to print the result--------------------------------------------

# def min_value(current_object):
#     return min(current_object)
#
# def max_value(current_object):
#     return max(current_object)
#
# def sum_of_elements(current_object):
#     return sum(current_object)
#
# numbers_list = [int(number) for number in input().split()]
#
# result_min = min_value(numbers_list)
# result_max = max_value(numbers_list)
# total_sum = sum_of_elements(numbers_list)
#
# print(f"The minimum number is {result_min}")
# print(f"The maximum number is {result_max}")
# print(f"The sum number is: {total_sum}")

# --------------------solution 2 - if we will always use and print all three ------------------------
def numbers_operations(current_object):
    print(f"The minimum number is {min(current_object)}")
    print(f"The maximum number is {max(current_object)}")
    print(f"The sum number is: {sum(current_object)}")

numbers_list = [int(number) for number in input().split()]

result = numbers_operations(numbers_list)