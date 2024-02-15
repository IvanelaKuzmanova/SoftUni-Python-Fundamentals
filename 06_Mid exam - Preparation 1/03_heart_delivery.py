needed_hearts = [int(x) for x in input().split("@")]
starting_index = 0
current_house_index = 0

while True:
    command = input()

    if command == "Love!":
        break

    splitted_command = command.split()
    jump_length = int(splitted_command[-1])

    if current_house_index + jump_length <= len(needed_hearts) - 1:     #if index is in range
        current_house_index += jump_length

        if needed_hearts[current_house_index] == 0:
            print(f"Place {current_house_index} already had Valentine's day.")
        else:
            needed_hearts[current_house_index] -= 2
            if needed_hearts[current_house_index] == 0:
                print(f"Place {current_house_index} has Valentine's day.")

    else:           #if index is out of range
        current_house_index = 0
        if needed_hearts[current_house_index] == 0:
            print(f"Place {current_house_index} already had Valentine's day.")
        else:
            needed_hearts[current_house_index] -= 2
            if needed_hearts[current_house_index] == 0:
                print(f"Place {current_house_index} has Valentine's day.")


zeroes = needed_hearts.count(0)
failed_houses = len(needed_hearts) - needed_hearts.count(0)
failed = False

if failed_houses > 0:
    failed = True

print(f"Cupid's last position was {current_house_index}.")

if not failed:
    print(f'Mission was successful.')
else:
    print(f"Cupid has failed {failed_houses} places.")