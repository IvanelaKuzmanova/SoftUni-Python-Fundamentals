text = input()

current_text = ""
current_repeat = ""

final_rage_message = ""

for index in range(len(text)):

    if not text[index].isdigit():
        current_text += text[index].upper()
    else:
        for next_char in range(index, len(text)):       #to check symbols after first digit, because number can be from more digits
            if not text[next_char].isdigit():       #once it reaches non digit symbol, sub loop breaks
                break
            current_repeat += text[next_char]

        final_rage_message += current_text * int(current_repeat)
        current_text = ""
        current_repeat = ""

print(f"Unique symbols used: {len(set(final_rage_message))}")
print(final_rage_message)