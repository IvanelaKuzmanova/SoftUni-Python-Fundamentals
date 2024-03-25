import re

#">>{furniture_name}<<{price}!{quantity}

pattern = r">>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"

bought_furniture = []
total_price = 0

while True:

    command = input()

    if command == "Purchase":
        break

    result = re.fullmatch(pattern, command)

    if result:

        bought_furniture.append(result["furniture"])
        total_price += float(result["price"]) * int(result["quantity"])

print(f"Bought furniture:")
for el in bought_furniture:
    print(el)
print(f"Total money spend: {total_price:.2f}")

#     if len(result) > 0:
#
#         bought_furniture.append(result[0][0])
#         total_price += float(result[0][1]) * int(result[0][5])
# #

