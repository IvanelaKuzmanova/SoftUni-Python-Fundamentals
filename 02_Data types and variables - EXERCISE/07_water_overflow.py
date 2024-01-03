tank_capacity = 255

count = int(input())

total_liters = 0

for i in range(count):
    liters = int(input())

    if liters > (tank_capacity - total_liters):
        print(f"Insufficient capacity!")
        continue
    else:
        total_liters += liters

print(f"{total_liters}")