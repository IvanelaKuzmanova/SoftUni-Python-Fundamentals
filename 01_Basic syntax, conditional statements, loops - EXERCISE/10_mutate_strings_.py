first_string = input()
second_string = input()

last_printed = first_string             #за да има с какво да сравняваме първият път за уникалност

for char_index in range(len(first_string)):

    left_part = second_string[:char_index + 1]         #от началото на стринга до символът, дефиниран от цикъла
    right_part = first_string[char_index + 1:]           # от символа, ефиниран от цикъла, до края на стринга
    new_string = left_part + right_part

    if new_string != last_printed:
        print(f"{new_string}")
        last_printed = new_string       #за да стравняваме за уникалност с последното принтирано, а не с първия стринг
