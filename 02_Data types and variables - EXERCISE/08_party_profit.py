group = int(input())
days = int(input())

total_profit = 0

for current_day in range(1, days + 1):

    if current_day % 10 == 0:           #all statements are separate ifs, because they should not be skipped (15th day is also 3rd and 5th)
        group -= 2
    if current_day % 15 == 0:
        group += 5

    total_profit += 50 - (2 * group)

    if current_day % 3 == 0:
        total_profit -= 3 * group
    if current_day % 5 == 0:
        total_profit += 20 * group
        if current_day % 3 == 0:
            total_profit -= 2 * group

profit_per_person = (total_profit // group)

print(f"{group} companions received {profit_per_person} coins each.")
