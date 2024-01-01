budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price + (0.25 * flour_price))/4

price_one_recipe = flour_price + eggs_price + milk_price

current_bread_count = 0
colored_eggs = 0

while budget > price_one_recipe:

    budget -= price_one_recipe
    current_bread_count += 1
    colored_eggs += 3

    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget :.2f}BGN left.")

