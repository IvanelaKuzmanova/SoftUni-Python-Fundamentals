def perfect_number(num):

    positive = True
    valid_divisors = []

    if num < 1:
        positive = False
        return "Number not positive"

    for divisor in range(1, num + 1):

        if num % divisor == 0:
            valid_divisors.append(int(divisor))

    if sum(valid_divisors) == num * 2:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())

check = perfect_number(number)

print(check)
