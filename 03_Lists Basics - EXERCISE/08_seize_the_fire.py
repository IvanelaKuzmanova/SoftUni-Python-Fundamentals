commands_as_list = input().split("#")
water_amount = int(input())

cells_put_out = []

total_effort = 0
total_fire = 0

for element in commands_as_list:
    command_separated = element.split(" = ")
    fire_type = command_separated[0]
    water_needed = int(command_separated[1])

    if fire_type == "High":
        if 81 <= water_needed <= 125:
            if water_amount < water_needed:
                continue
            water_amount -= int(water_needed)
            total_effort += 0.25 * water_needed
            cells_put_out.append(water_needed)
            total_fire += water_needed

    elif fire_type == "Medium":
        if 51 <= water_needed <= 80:
            if water_amount < water_needed:
                continue
            water_amount -= int(water_needed)
            total_effort += 0.25 * water_needed
            cells_put_out.append(water_needed)
            total_fire += water_needed

    elif fire_type == "Low":
        if 1 <= water_needed <= 50:
            if water_amount < water_needed:
                continue
            water_amount -= int(water_needed)
            total_effort += 0.25 * water_needed
            cells_put_out.append(water_needed)
            total_fire += water_needed

print(f"Cells:")

for cell in range(len(cells_put_out)):
    print(f" - {cells_put_out[cell]}")

print(f"Effort: {total_effort :.2f}")
print(f"Total Fire: {total_fire}")




