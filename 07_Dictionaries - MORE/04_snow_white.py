dwarfs_register = {}

while True:

    command = input()

    if command == "Once upon a time":
        break

    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)

    if hat_color not in dwarfs_register.keys():
        dwarfs_register[hat_color] = {}

    if name not in dwarfs_register[hat_color].keys():
        dwarfs_register[hat_color][name] = physics
    else:
        if dwarfs_register[hat_color][name] < physics:
            dwarfs_register[hat_color][name] = physics

#--------------------------------------------------------------------------


