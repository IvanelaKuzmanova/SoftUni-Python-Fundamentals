import re

text = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

result = re.findall(pattern, text, re.I)

print(len(result))