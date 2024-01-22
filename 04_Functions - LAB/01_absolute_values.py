numbers_list = input().split()
absolute_list = []

for num in numbers_list:
    absolute_list.append(abs(float(num)))       #floar needed since num is still stirng in the upper list

print(absolute_list)