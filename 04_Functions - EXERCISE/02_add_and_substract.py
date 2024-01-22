def sum_numbers(num1, num2):
    result = num1 + num2
    return result

def substract(new_num, num3):
    return new_num - num3

num1 = int(input())
num2 = int(input())
num3 = int(input())

summed = sum_numbers(num1, num2)
difference = substract(summed, num3)

print(difference)