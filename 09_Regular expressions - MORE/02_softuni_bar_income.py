import re

pattern = (r"%(?P<name>[A-Z][a-z]+)%"    #NAME
           r"([^\|\$\.%]+)?"        #---> Between each part there can be other symbols, except ('|', '$', '%' and '.')
           r"<(?P<product>\w+)>"    #PRODUCT
           r"([^\|\$\.%]+)?"    #---> Between each part there can be other symbols, except ('|', '$', '%' and '.')
           r"\|([^\|\$\.%]+0-9)?(?P<count>\d+)([^\|\$\.%]+)?\|"    #COUNT
           r"([^\|\$\.%0-9]+)?"    #---> Between each part there can be other symbols, except ('|', '$', '%' and '.')
           r"(?P<price>\d+(\.\d+)?)([^\|\$\.%]+)?\$")    #PRICE
total_price = 0
command = input()

while command != "end of shift":
    matches = re.match(pattern, command)
    if matches:
        matches_as_dict = matches.groupdict()
        current_price = int(matches_as_dict['count']) * float(matches_as_dict['price'])
        total_price += current_price
        print(f"{matches_as_dict['name']}: {matches_as_dict['product']} - {current_price :.2f}")
        current_price = 0
    command = input()

print(f"Total income: {total_price :.2f}")
