import re

text = input()

pattern = r"(@+|#+)(?P<color>[a-z]{3,})(@+|#+)([^A-Za-z\d]+)*(\/+)(?P<amount>\d+)(\/+)"

result = [el.group() for el in re.finditer(pattern, text)]

for element in result:
    current_color = ""
    current_amount = ""
    for char in element:
        if char.isalpha():
            current_color += char
        elif char.isdigit():
            current_amount += char

    print(f'You found {current_amount} {current_color} eggs!')
