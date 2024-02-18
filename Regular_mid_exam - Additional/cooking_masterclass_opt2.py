import math

budget = float(input())
students_number = int(input())
flour_price = float(input())
egg_price = float(input())          #for one egg
apron_price = float(input())

flour_packages_discount = 0

for person in range(1, students_number + 1):

    if person % 5 == 0:
        flour_packages_discount += 1

total_money_needed = ((students_number - flour_packages_discount) * flour_price + \
                      students_number * 10 * egg_price + \
                      math.ceil(1.2 * students_number) * apron_price)

if total_money_needed <= budget:
    print(f"Items purchased for {total_money_needed:.2f}$.")
else:
    print(f"{abs(budget - total_money_needed):.2f}$ more needed.")