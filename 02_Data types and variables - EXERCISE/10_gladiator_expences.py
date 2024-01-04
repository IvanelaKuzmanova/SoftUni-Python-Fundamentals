lost_battles = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
total_money = 0

for fight in range(1, lost_battles + 1):

    if fight % 2 == 0:
        total_money += helmet_price
        broken_helmet += 1
    if fight % 3 == 0:
        total_money += sword_price
        broken_sword += 1
        if fight % 2 == 0:
            total_money += shield_price
            broken_shield += 1

    if broken_shield % 2 == 0 and broken_shield != 0:
        total_money += armor_price
        broken_armor += 1

print(f"Gladiator expenses: {total_money :.2f} aureus")