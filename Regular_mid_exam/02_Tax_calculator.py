vehicles_list = input().split(">>")
total_taxes_collected = 0

for vehicle_info in vehicles_list:

    separated_info = vehicle_info.split()
    car_type = separated_info[0]
    years_to_pay = int(separated_info[1])
    kilometers_traveled = int(separated_info[2])

    if car_type == "family":
        initial_tax = 50
        yearly_reduction = years_to_pay * 5
        kilometers_increase = (kilometers_traveled // 3000) * 12

        total_car_tax = initial_tax + kilometers_increase - yearly_reduction
        total_taxes_collected += total_car_tax
        print(f"A {car_type} car will pay {total_car_tax:.2f} euros in taxes.")

    elif car_type == "heavyDuty":
        initial_tax = 80
        yearly_reduction = years_to_pay * 8
        kilometers_increase = (kilometers_traveled // 9000) * 14

        total_car_tax = initial_tax + kilometers_increase - yearly_reduction
        total_taxes_collected += total_car_tax
        print(f"A {car_type} car will pay {total_car_tax:.2f} euros in taxes.")

    elif car_type == "sports":
        initial_tax = 100
        yearly_reduction = years_to_pay * 9
        kilometers_increase = (kilometers_traveled // 2000) * 18

        total_car_tax = initial_tax + kilometers_increase - yearly_reduction
        total_taxes_collected += total_car_tax
        print(f"A {car_type} car will pay {total_car_tax:.2f} euros in taxes.")

    else:
        print("Invalid car type.")
        continue

print(f"The National Revenue Agency will collect {total_taxes_collected:.2f} euros in taxes." )

