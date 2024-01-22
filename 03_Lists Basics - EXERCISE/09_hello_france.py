ticket_price = 150

collection = input().split("|")
budget = float(input())

items_acc_to_condition = []
bought_items = []
collected_money = 0
items_list = []
spent_money = 0

for item in collection:
    items_list.append(item.split("->"))

for item in items_list:
    if item[0] == "Clothes" and float(item[1]) <= 50:
        items_acc_to_condition.append(float(item[1]))
    elif item[0] == "Shoes" and float(item[1]) <= 35:
        items_acc_to_condition.append(float(item[1]))
    elif item[0] == "Accessories" and float(item[1]) <= 20.50:
        items_acc_to_condition.append(float(item[1]))

for price in items_acc_to_condition:
    if price <= budget:
        budget -= price
        spent_money += price
        bought_items.append(str(price))

for price in bought_items:
    increased_price = float(price) * 1.40
    print(f"{increased_price :.2f}", end = " ")
    collected_money += increased_price

profit = collected_money - spent_money
print()
print(f"Profit: {profit :.2f}")

if budget + collected_money >= ticket_price:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")

 # sold_items[price] = current_price       #replacing element on current index with higher price
    # sold_items[price] = "%.2f" % sold_items[price]         #formatting element to 2nd decimal place