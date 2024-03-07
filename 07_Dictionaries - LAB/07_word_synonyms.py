count_keys = int(input())
synonyms = {}

for _ in range(count_keys):

    key = input()
    synonym = input()

    if key not in synonyms.keys():
        synonyms[key] = []
    synonyms[key].append(synonym)

for element in synonyms:
    print(f'{element} - {", ".join(synonyms[element])}')