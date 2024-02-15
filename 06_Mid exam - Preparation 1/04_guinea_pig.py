food = float(input())
hay = float(input())
cover = float(input())
pig_weight = float(input())

daily_food = 0.3

enough = True

for day in range(1, 30 + 1):        #one month

    food -= daily_food      #everyday pig eats 300g
    if food <= 0:
        enough = False
        break

    if day % 2 == 0:
        hay -= 0.05 * food
        if hay <= 0:
            enough = False
            break

    if day % 3 == 0:
        cover -= pig_weight / 3
        if cover <= 0:
            enough = False
            break

if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")

else:
    print(f"Merry must go to the pet store!")

