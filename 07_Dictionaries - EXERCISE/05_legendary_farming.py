legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

command = input().split()

won = False

while not won:
    for index in range(0, len(command) - 1, 2):
        if not won:
            quantity = int(command[index])
            material = command[index + 1].lower()

            if material in key_materials:
                key_materials[material] += quantity
                if key_materials[material] >= 250:
                    key_materials[material] -= 250
                    won = True
                    print(f"{legendary_items[material]} obtained!")
            else:
                if material not in junk:
                    junk[material] = 0
                junk[material] += quantity
    if not won:
        command = input().split()

#--------------------------------------------------------------------------------

for key, value in key_materials.items():
    print(f"{key}: {value}")

for key, value in junk.items():
    print(f"{key}: {value}")



