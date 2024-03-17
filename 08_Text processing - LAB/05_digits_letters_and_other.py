text = input()
numbers = ""
letters = ""
symbols = ""

# numbers_list = [num for num in text if num.isdigit()]
# letters_list = [letter for letter in text if letter.isalpha()]

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(f"{numbers}\n{letters}\n{symbols}")