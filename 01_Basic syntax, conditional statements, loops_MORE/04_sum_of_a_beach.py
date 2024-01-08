text = input()

lowercase = text.lower()

sand = lowercase.count("sand")
water = lowercase.count("water")
fish = lowercase.count("fish")
sun = lowercase.count("sun")

total = sand + water + fish + sun

print(total)