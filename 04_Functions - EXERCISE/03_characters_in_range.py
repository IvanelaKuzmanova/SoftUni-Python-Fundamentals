def ascii_symbols_between(element1, element2):
    chars_list = []
    for char in range(ord(element1) + 1, ord(element2)):
        chars_list.append(chr(char))

    return chars_list


symbol1 = input()
symbol2 = input()

print(" ".join(ascii_symbols_between(symbol1, symbol2)))
