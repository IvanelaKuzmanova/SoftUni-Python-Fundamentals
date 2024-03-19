all_text = input().split()    #number between two letters
total_result = 0

for current_text in all_text:
    first_letter = current_text[0]
    last_letter = current_text[-1]
    current_number = int(current_text[1: len(current_text) - 1])   #from 1, since 0 is letter, to -1, since end is exclusive

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64          #using ascii table - 64 since letter is on 64th position there
        total_result += current_number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_result += current_number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_result -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_result += last_letter_position

print(f"{total_result:.2f}")

