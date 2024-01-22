def total_price(prodyct_type, quantity):

    price = 0

    if prodyct_type == "coffee":
        price = 1.50
    elif prodyct_type == "water":
        price = 1.00
    elif prodyct_type == "coke":
        price = 1.40
    elif prodyct_type == "snacks":
        price = 2.00

    return price * quantity


product_type = input()
quantity = int(input())

result = float(total_price(product_type, quantity))

print(f"{result :.2f}")