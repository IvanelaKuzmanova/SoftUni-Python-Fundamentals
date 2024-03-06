products_dict = {}

while True:
    command = input()

    if command == "statistics":
        break

    contents = command.split(": ")
    product = contents[0]
    quantity = int(contents[1])

    if product not in products_dict:
        products_dict[product] = 0          #if key not existing, we make sure to add it
    products_dict[product] += quantity      # adding new quantity to the existing one

print(f"Products in stock:")

for key, value in products_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products_dict.keys())}")
print(f"Total Quantity: {sum(products_dict.values())}")
