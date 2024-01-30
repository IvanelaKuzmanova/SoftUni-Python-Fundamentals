def negatives_check(numbers_list):
    count_negatives = 0

    for n in numbers_list:
        if n < 0:
            count_negatives += 1
        if n == 0:
            return "zero"


    if count_negatives % 2 == 0:
        return "positive"
    else:
        return "negative"


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

nums_list = [number_1, number_2, number_3]

result = negatives_check(nums_list)
print(result)

