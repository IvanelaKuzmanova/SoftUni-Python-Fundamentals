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
colors_list = []
dwarfs_list = []
physics_list = []


for key, value in dwarfs_register.items():

    colors_list.append(key)

    for k, v in value.items():

        dwarfs_list.append(k)
        physics_list.append(v)

# for index in range(1, len(dwarfs_list + 1):
#
#     current_tuple =

tupled_list = list(zip(colors_list, dwarfs_list, physics_list))

print(sorted(tupled_list, key=lambda x: (x[2], x[1]), reverse=True))