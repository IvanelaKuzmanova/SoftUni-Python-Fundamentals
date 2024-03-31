import re
pattern = r"\|(?P<name>[A-Z]{4,})\|:#(?P<title>[A-Za-z]+ [A-Za-z]+)#"

lines_count = int(input())

for text in range(lines_count):

    current_text = input()

    valid_result = re.fullmatch(pattern, current_text)

    if valid_result:
        print(f'{valid_result["name"]}, The {valid_result["title"]}')
        print(f'>> Strength: {len(valid_result["name"])}')
        print(f">> Armor: {len(valid_result['title'])}")

    else:
        print("Access denied!")
