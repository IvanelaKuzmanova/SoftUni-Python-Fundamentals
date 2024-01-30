names_list = input().split(", ")

sorted_names = sorted(names_list, key=lambda name: (-len(name), name))      #lambda function to sort first by len with reversed order (-len) and then alphabetically (name)

print(sorted_names)