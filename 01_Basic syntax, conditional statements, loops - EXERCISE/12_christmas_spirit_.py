decorations_quantity = int(input())
days_left = int(input())

money_needed = 0
spirit_improvement = 0
days_counter = 0

for day in range(1, days_left + 1):

    if day % 11 == 0:
        decorations_quantity += 2

    if day % 2 == 0:
        money_needed += decorations_quantity * 2
        spirit_improvement += 5

    if day % 3 == 0:
        money_needed += decorations_quantity * (5 + 3)
        spirit_improvement += (3 + 10)           #+30

    if day % 5 == 0:
        money_needed += decorations_quantity * 15
        spirit_improvement += 17
        if day % 3 == 0:
            spirit_improvement += 30            #aко в условието е написано като подбулет, и тук е вложена проверка (не отделна)

    if day % 10 == 0:
        spirit_improvement -= 20
        money_needed += (5 + 3 +15)

    days_counter += 1

if days_counter % 10 == 0:
    spirit_improvement -= 30

print(f"Total cost: {money_needed}")
print(f"Total spirit: {spirit_improvement}")

