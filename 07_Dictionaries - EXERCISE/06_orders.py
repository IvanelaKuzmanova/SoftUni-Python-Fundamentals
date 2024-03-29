products = {}

while True:

    command = input().split()

    if command[0] == "buy":
        break

    name = command[0]
    current_price = float(command[1])
    current_quantity = float(command[2])
    starting_info = {"price": 0, "quantity": 0}

    if name not in products.keys():
        products[name] = starting_info

    products[name]["price"] = current_price
    products[name]["quantity"] += current_quantity

for product, value in products.items():
    print(f"{product} -> {value['price'] * value['quantity'] :.2f}")