content = input().split(" ")
bakery_dict = {}

for i in range(0, len(content), 2):     #starting from index 0 and using step 2
    key = content[i]            #creatng keys
    value = content[i+1]        #creating values
    bakery_dict[key] = int(value)           #assigning value to the key

print(bakery_dict)
