year = int(input())

special = False

while not special:

    year += 1
    year_as_string = str(year)

    if len(year_as_string) == len(set(year_as_string)):
        special = True
        break

print(year)