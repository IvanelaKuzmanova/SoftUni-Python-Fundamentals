number = int(input())
word = input()

strings_list = []

for _ in range(number):
    current_string = input()
    strings_list.append(current_string)
print(strings_list)

for i in range(len(strings_list) - 1, -1, -1):          #iterating it from backwards, so we do not skip and element while removing (beacause of using len)
    element = strings_list[i]

    if word not in element:
        strings_list.remove(element)
print(strings_list)
