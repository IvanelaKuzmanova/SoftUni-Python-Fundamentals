string_one, string_two = input().split()

final_sum = 0

if len(string_one) > len(string_two):
    for index in range(len(string_two)):
        final_sum += ord(string_one[index]) * ord(string_two[index])
    for index in range(len(string_two), len(string_one)):
        final_sum += ord(string_one[index])

elif len(string_two) > len(string_one):
    for index in range(len(string_one)):
        final_sum += ord(string_one[index]) * ord(string_two[index])
    for index in range(len(string_one), len(string_two)):
        final_sum += ord(string_two[index])

else:
    for index in range(len(string_one)):
        final_sum += ord(string_one[index]) * ord(string_two[index])

print(final_sum)