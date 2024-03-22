import re

pattern = r"\d+"
numbers_list = []

text_line = input()

while text_line:

    result = re.findall(pattern, text_line)
    numbers_list.extend(result)
    text_line = input()

print(*numbers_list)