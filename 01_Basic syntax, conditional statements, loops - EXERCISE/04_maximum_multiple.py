divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor - 1, -1):         #рейндж на обратно, защото търсим най-голямото. Важно е да посочим стъпка -1!

    if number % divisor == 0:
        print(number)
        break



