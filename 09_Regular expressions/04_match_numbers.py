import re
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

text = input()

result = re.finditer(pattern, text)         #using iter since the result is tupled list

for element in result:
    print(element.group(), end=" ")         #.group to combine all elements from each tuple
