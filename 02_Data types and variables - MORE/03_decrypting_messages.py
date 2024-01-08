key = int(input())
rows = int(input())

for i in range(rows):
    letter = input()
    corresponding_number = ord(letter)
    new_number = corresponding_number + key
    new_letter = chr(new_number)

    print(new_letter, end = "")