import re

# pattern = r"([a-zA-Z0-9\.\-\_]+)@([a-zA_Z]+\.[a-zA-Z]+\.[a-zA-Z]+|[a-zA_Z]+\.[a-zA-Z]+)+"

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+([\._-][a-zA-Z0-9]+)?@[a-zA-Z]+(-[a-zA-Z]+)?(\.[a-zA-Z]+(-[a-zA-Z]+)?)+"
text = input()

result = [el.group() for el in re.finditer(pattern, text)]

for element in result:
    print(element)

