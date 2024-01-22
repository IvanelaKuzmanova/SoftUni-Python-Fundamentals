def total_price(product_type, quantity):

    if product_type == "coffee":
        return f"{1.50 * quantity:.2f}"
    elif product_type == "water":
        return f"{1.00 * quantity:.2f}"
    elif product_type == "coke":
        return f"{1.40 * quantity:.2f}"
    elif product_type == "snacks":
        return f"{2.00 * quantity:.2f}"


product_type = input()
quantity = int(input())

result = total_price(product_type, quantity)

print(result)
