ticket_price = 150

collection = input().split("|")
budget = float(input())

sold_items = []
increased_prices = []
collected_money = 0

for item in range(len(collection)):
    items_list = collection[item].split("->")
    item_type = items_list[0]
    item_price = float(items_list[1])

    if item_price <= budget:
        if (item_type == "Clothes" and item_price <= 50) or \
            (item_type == "Shoes" and item_price <= 35) or \
            (item_type == "Accessories" and item_price <= 20.50):
            budget -= item_price
            sold_items.append(item_price)

for price in range(len(sold_items)):
    current_price = float(sold_items[price])
    current_price *= (1 + 0.40)
    current_price = round(current_price, 2)
    increased_prices.append(current_price)
    # sold_items[price] = current_price       #replacing element on current index with higher price
    # sold_items[price] = "%.2f" % sold_items[price]         #formatting element to 2nd decimal place
profit = sum(increased_prices) - sum(sold_items)

print(*increased_prices, sep=" ")
print(f"Profit: {profit :.2f}")

if budget + sum(increased_prices) >= ticket_price:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")

