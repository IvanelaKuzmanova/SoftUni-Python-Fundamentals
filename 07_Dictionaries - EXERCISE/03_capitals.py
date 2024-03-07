country_names = input().split(", ")
capital_names = input().split(", ")

dictionary = dict(zip(country_names, capital_names))

for key, value in dictionary.items():
    print(f"{key} -> {value}")