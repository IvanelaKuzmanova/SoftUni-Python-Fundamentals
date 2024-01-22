def calculator(operator_type, num1, num2):

    if operator_type == "multiply":
        return num1 * num2
    elif operator_type == "divide":
        return int(num1 / num2)         #to result int number
    elif operator_type == "add":
        return num1 + num2
    elif operator_type == "subtract":
        return num1 - num2

operator_type = input()
num1 = int(input())
num2 = int(input())

result = calculator(operator_type, num1, num2)

print(result)
