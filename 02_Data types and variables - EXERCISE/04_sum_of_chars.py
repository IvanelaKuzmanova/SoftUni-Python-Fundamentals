number_of_lines = int(input())
sum = 0

for i in range(number_of_lines):

    letter = input()
    num = ord(letter)
    sum += num

print(f"The sum equals: {sum}")