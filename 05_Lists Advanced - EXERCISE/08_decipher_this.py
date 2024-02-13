def deciphing_messages(message:str) -> str:

    new_message = []

    for word in message:

        word_digits = []
        word_letters = []
        new_word = []

        for char in word:

            if char.isdigit():
                word_digits.append(char)
            else:
                word_letters.append(char)

        code = int(''.join(word_digits))
        letter_from_code = chr(code)
        new_word.append(letter_from_code)

        word_letters[0], word_letters[-1] = word_letters[-1], word_letters[0]

        for element in word_letters:
            new_word.append(element)

        new_message.append(''.join(new_word))

    return ' '.join(new_message)


current_message = input().split()
result = deciphing_messages(current_message)
print(result)