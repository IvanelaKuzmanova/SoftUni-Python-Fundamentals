def even_odd_check(number):

    even_list = []
    odd_list = []

    for digit in number:
        if int(digit) % 2 == 0:
            even_list.append(int(digit))
        else:
            odd_list.append(int(digit))

    return f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}"


number = input()

result = even_odd_check(number)

print(result)