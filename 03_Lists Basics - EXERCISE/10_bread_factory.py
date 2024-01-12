energy = 100
coins = 100

bakery_closed = False

events_as_string = input().split("|")       #creating full list of all commands

for command in events_as_string:
    command_as_list = command.split("-")          #in each iteration separating each command to list of separate components

#for command in events_as_string:
    # command_type, value = command.split("-")                  Way of direct splitting of two values

    if command_as_list[0] == "rest":        #if in the current command on index 0 stays rest
        energy += int(command_as_list[1])
        if energy > 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            print(f"You gained {command_as_list[1]} energy.")
        print(f"Current energy: {energy}.")

    elif command_as_list[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += int(command_as_list[1])
            print(f"You earned {command_as_list[1]} coins.")
        elif energy < 30:
            energy += 50
            print(f"You had to rest!")

    else:           #in any other case (as written in the task)
        if coins >= int(command_as_list[1]):
            print(f"You bought {command_as_list[0]}.")
            coins -= int(command_as_list[1])
        elif coins < int(command_as_list[1]):
            print(f"Closed! Cannot afford {command_as_list[0]}.")
            bakery_closed = True
            break

if not bakery_closed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")



