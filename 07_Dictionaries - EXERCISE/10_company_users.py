employees_dict = {}

while True:

    command = input().split(" -> ")

    if command[0] == "End":
        break

    company = command[0]
    employee_id = command[1]

    if company not in employees_dict.keys():
        employees_dict[company] = []

    if employee_id not in employees_dict[company]:
        employees_dict[company].append(employee_id)

for key, value in employees_dict.items():
    print(f"{key}")

    for element in value:
        print(f"-- {element}")