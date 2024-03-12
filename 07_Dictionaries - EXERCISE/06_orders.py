products = {}

while True:

    command = input().split()

    if command[0] == "buy":
        break

    name = command[0]
    current_price = float(command[1])
    current_quantity = float(command[2])
    current_info = {"price": current_price, "quantity": current_quantity}

    if name not in products.keys():
        products[name] = current_info

    elif name in products.keys():
        products[name]["price"] = current_price
        products[name]["quantity"] += current_quantity

print(products)