range_start = int(input())
range_end = int(input())

for symbol in range(range_start, range_end + 1):

    value = chr(symbol)
    print(f"{value}", end=" ")