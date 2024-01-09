numbers_count = int(input())

list_positive = []
list_negative = []

for i in range(numbers_count):
    current_number = int(input())

    if current_number >= 0:
        list_positive.append(current_number)
    else:
        list_negative.append(current_number)

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}\nSum of negatives: {sum(list_negative)}")

