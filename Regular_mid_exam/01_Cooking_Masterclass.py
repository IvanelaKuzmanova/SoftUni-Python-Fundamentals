import math

budget = float(input())
students = int(input())

flour_package_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

free_flour_packages = 0

for student in range(1, students + 1):

    if student % 5 == 0:
        free_flour_packages += 1

money_for_flour = (students - free_flour_packages) * flour_package_price
money_for_eggs = students * 10 * single_egg_price
money_for_apron = math.ceil(1.2 * students) * single_apron_price

total_money_needed = money_for_flour + money_for_eggs + money_for_apron
difference = abs(budget - total_money_needed)

if total_money_needed <= budget:
    print(f"Items purchased for {total_money_needed:.2f}$.")
else:
    print(f"{difference:.2f}$ more needed.")



