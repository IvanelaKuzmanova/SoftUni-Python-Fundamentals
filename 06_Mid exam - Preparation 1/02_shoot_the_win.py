targets_values = [int(x) for x in input().split()]

command = input()

shot_targets_count = 0

while command != "End":

    current_index = int(command)

    if current_index <= len(targets_values) - 1:        #if there is a value on the given index

        shot_targets_count += 1         #one shot considered
        shot_target_value = targets_values[current_index]         #keeping track of the shot value
        targets_values[current_index] = -1

        for index in range(len(targets_values)):

            if targets_values[index] != -1:
                if targets_values[index] > shot_target_value:
                    targets_values[index] -= shot_target_value
                elif targets_values[index] <= shot_target_value:
                    targets_values[index] += shot_target_value

    command = input()

list_for_printing = " ".join(str(item) for item in targets_values)

print(f'Shot targets: {shot_targets_count} -> {list_for_printing}')