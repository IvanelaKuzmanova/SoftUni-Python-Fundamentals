orders_count = int(input())
total_price = 0

for _ in range(orders_count):

    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if not 0.01 <= price_per_capsule <= 100.00:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsules_needed <= 2000:
        continue

    price_coffee = price_per_capsule * days * capsules_needed
    total_price += price_coffee

    print(f"The price for the coffee is: ${price_coffee :.2f}")

print(f"Total: ${total_price :.2f}")
