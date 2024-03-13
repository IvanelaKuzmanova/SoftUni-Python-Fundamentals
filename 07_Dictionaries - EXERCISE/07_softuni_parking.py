commands_count = int(input())
registered_cars = {}

for _ in range(commands_count):

    splitted_command = input().split()

    command = splitted_command[0]
    username = splitted_command[1]

    if command == "register":

        license_number = splitted_command[2]

        if username in registered_cars.keys():
            print(f'ERROR: already registered with plate number {license_number}')

        else:
            registered_cars[username] = license_number
            print(f'{username} registered {license_number} successfully')


    elif command == "unregister":

        if username not in registered_cars.keys():
            print(f"ERROR: user {username} not found")
        else:
            registered_cars.pop(username)
            print(f"{username} unregistered successfully")


for car, number in registered_cars.items():
    print(f"{car} => {number}")