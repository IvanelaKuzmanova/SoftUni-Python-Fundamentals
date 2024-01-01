number = int(input())

for i in range(1, number + 1):          #prints stars from 1 to the number inclusive
    for j in range(0, i):           #uses index positions from 0 to i-1
        print("*", end="")
    print()                     #new line after printing all the stars on the previous line

for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()