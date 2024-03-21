import re

pattern = r"(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})"        #\2 repeats the second group

text = input()

result = re.findall(pattern, text)

for element in result:

    day = element[0]
    month = element[2]
    year = element[3]

    print(f"Day: {day}, Month: {month}, Year: {year}")