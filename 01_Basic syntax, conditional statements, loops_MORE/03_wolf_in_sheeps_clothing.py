animals_splitted = input().split(", ")
animals_splitted.reverse()

if animals_splitted.index("wolf") == 0:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {animals_splitted.index("wolf")}! You are about to be eaten by a wolf!')