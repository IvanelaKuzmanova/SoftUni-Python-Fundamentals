start = ord(input())
end = ord(input())

text = input()
total_sum = 0

for char in text:

    if start < ord(char) < end:
        total_sum += ord(char)

print(total_sum)