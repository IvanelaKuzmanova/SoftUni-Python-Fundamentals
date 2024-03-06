content = input().split(" ")
products_dict = {}

for i in range(0, len(content), 2):     #starting from index 0 and using step 2
    key = content[i]                    #creatng keys
    value = content[i+1]                #creating values
    products_dict[key] = int(value)           #assigning value to the key

products_to_search = input().split()

for product in products_to_search:
    if product in products_dict:
        print(f"We have {products_dict[product]} of {product} left")        #if the string is found in dictionary, we use it to take first the key, then the value
    else:
        print(f"Sorry, we don't have {product}")

