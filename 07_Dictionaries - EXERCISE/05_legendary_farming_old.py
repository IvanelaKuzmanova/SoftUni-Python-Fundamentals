key_materials = {}
junk = {}

not_won = True

while not_won:

    command = input().split()

    for index in range(0, len(command), 2):

        value = command[index]
        key = command[index + 1].lower()            #case insensitive

        if key == "motes" or key == "fragments" or key == "shards":
            if key not in key_materials.keys():
                key_materials[key] = int(value)
                if key_materials[key] >= 250:
                    not_won = False
                    break
            else:
                key_materials[key] += int(value)
                if key_materials[key] >= 250:
                    not_won = False
                    break

        else:
            if key not in junk.keys():
                junk[key] = int(value)
            else:
                junk[key] += int(value)


for key, value in key_materials.items():
    if value >= 250:
        if key == "shards":
            print(f"Shadowmourne obtained!")
        elif key == "motes":
            print(f"Dragonwrath obtained!")
        elif key == "fragments":
            print(f"Valanyr obtained!")

        key_materials[key] -= 250

for key, value in key_materials.items():
    print(f"{key}: {value}")

for key, value in junk.items():
    print(f"{key}: {value}")



