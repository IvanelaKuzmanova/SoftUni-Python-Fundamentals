lines = int(input())
balanced = False
open = 0
closed = 0

for i in range(lines):
    symbol = input()

    if symbol == "(":
        open += 1
        if open % 2 == 0 and closed == 0:
            balanced = False
            break

    elif symbol == ")":
        closed += 1
        if open == 0:
            balanced = False
            break


if open - closed == 0:
    balanced = True

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")