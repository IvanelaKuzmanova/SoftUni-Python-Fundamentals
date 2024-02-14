needed_hearts = [int(x) for x in input().split("@")]

command = input()

while command != 'Love!':

    splitted_command = command.split()
    jump_length = int(splitted_command[-1])
    starting_index = 0
    last_position = 0

    for _ in needed_hearts:

        current_house_index = starting_index + jump_length
        last_position = starting_index + jump_length

        if current_house_index > len(needed_hearts) - 1:
            current_house_index = 0
            starting_index = 0
            last_position = 0

        current_house_value = needed_hearts[current_house_index]

        if current_house_value == 0:
            print(f"Place {current_house_index} already had Valentine's day.")          #if house already has needed hearts, we skip it
            starting_index = current_house_index
            command = input()
            continue

        house_new_value = current_house_value - 2

        if house_new_value == 0:
            print(f"Place {current_house_index} has Valentine's day.")

        needed_hearts[current_house_index] = house_new_value            #replacing element with new value

        starting_index = current_house_index



    command = input()

print(f"Cupid's last position was {last_position}.")