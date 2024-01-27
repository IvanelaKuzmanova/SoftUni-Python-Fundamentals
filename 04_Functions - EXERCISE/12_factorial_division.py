import math

def factorials_division(num1 = int, num2 = int) -> int:
    factorial_1 = math.factorial(num1)
    factorial_2 = math.factorial(num2)
    return factorial_1 / factorial_2


number_1 = int(input())
number_2 = int(input())

result = factorials_division(number_1, number_2)

print(f"{result :.2f}")
