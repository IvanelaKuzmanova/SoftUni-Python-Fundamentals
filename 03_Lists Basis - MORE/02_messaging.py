numbers = input().split()
text = input()

summed_numbers = []

for number in numbers:
    sum_digits = 0
    for digit in number:
        sum_digits += int(digit)
    summed_numbers.append(sum_digits)

