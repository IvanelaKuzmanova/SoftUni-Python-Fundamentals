def numbers_checking(current_list):
    positives = []
    negatives = []
    even = []
    odd = []

    for number in current_list:

        if number >= 0:
            positives.append(number)
        else:
            negatives.append(number)

        if number % 2 == 0 or number == 0:
            even.append(number)
        else:
            odd.append(number)

    return f'Positive: {", ".join(str(digit) for digit in positives)}\nNegative: {", ".join(str(digit) for digit in negatives)}\nEven: {", ".join(str(digit) for digit in even)}\nOdd: {", ".join(str(digit) for digit in odd)}'


numbers_list = [int(x) for x in input().split(', ')]

result = numbers_checking(numbers_list)
print(result)





