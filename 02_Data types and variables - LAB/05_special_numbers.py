number = int(input())
special = False

for num in range(1, number + 1):

    num_as_string = str(num)
    digits_sum = 0

    for digit in num_as_string:
        digits_sum += int(digit)

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        special = True
        print(f"{num} -> {special}")
    else:
        print(f"{num} -> {special}")
