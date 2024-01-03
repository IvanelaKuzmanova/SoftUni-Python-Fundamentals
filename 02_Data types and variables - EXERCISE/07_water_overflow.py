tank_capacity = 255

count = int(input())

total_liters = 0

for i in range(count):
    liters = int(input())
    total_liters += liters

    if total_liters > tank_capacity:
        print(f"Insufficient capacity!")
        continue

print(f"{total_liters}")