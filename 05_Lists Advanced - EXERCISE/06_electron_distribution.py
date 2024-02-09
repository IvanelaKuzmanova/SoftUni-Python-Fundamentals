def filling_electrones(number_of_electrons:int) -> list:
    filled_shells = []
    current_shell_number = 1

    while number_of_electrons > 0:

        current_shell_electrons = 2 * current_shell_number ** 2

        if number_of_electrons >= current_shell_electrons:
            filled_shells.append(current_shell_electrons)       #if there are enough electrons we append a full shell
        else:
            filled_shells.append(number_of_electrons)       #if not enough electrones - we append all electrones left

        number_of_electrons -= current_shell_electrons
        current_shell_number += 1

    return filled_shells


electrones_number = int(input())
filling = filling_electrones(electrones_number)
print(filling)