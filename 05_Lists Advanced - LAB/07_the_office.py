
def average_happiness(happiness):

    average_happiness = max(happiness) / 2
    happy_count = 0

    for person in happiness:
        if person >= average_happiness:
            happy_count += 1

    if happy_count >= len(happiness)/2:
        return f"Score: {happy_count}/{len(happiness)}. Employees are happy!"
    else:
        return f"Score: {happy_count}/{len(happiness)}. Employees are not happy!"


happiness_list = [int(num) for num in input().split()]
improvement_factor = int(input())

total_happiness = [num * improvement_factor for num in happiness_list]

check = average_happiness(total_happiness)
print(check)
