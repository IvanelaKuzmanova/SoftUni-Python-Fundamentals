number = int(input())
prime = True

for i in range(2, number):          #it is described to be larger than 1 in the word file, that is why range starts from 2
    if number % i == 0:
        prime = False
        break

print(prime)


