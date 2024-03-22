import re

pattern = r"((?<= _)|(?<=^_))[a-zA-Z0-9]+\b"
text = input()

valid_names = [element.group() for element in re.finditer(pattern, text)]

print(*valid_names, sep=",")

