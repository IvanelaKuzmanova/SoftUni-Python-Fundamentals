numbers_count = int(input())

list_positive = []
list_negative = []
negatives_sum = 0
positives_count = 0

for i in range(numbers_count):
    current_number = int(input())

    if current_number >= 0:
        positives_count += 1
        list_positive.append(current_number)
    else:
        negatives_sum += current_number
        list_negative.append(current_number)

print(list_positive)
print(list_negative)
print(f"Count of positives: {positives_count}\nSum of negatives: {negatives_sum}")

