import re

racers_list = input().split(", ")
racers_dict = {}

pattern = r"\d|[a-z]|[A-Z]"

while True:

    command = input()
    current_racer = ""
    current_km = 0

    if command == "end of race":
        break

    matching_chars = re.findall(pattern, command)

    for el in matching_chars:
        if el.isalpha():
            current_racer += el
        else:
            current_km += int(el)

    if current_racer in racers_list and current_racer not in racers_dict.keys():
        racers_dict[current_racer] = current_km
    elif current_racer in racers_list and current_racer in racers_dict.keys():
        racers_dict[current_racer] += current_km

#----------------------------------------------------------------------------------
winners_list = (sorted(racers_dict.items(), key=lambda x:x[1], reverse=True)[:3])

print(f"1st place: {winners_list[0][0]}")
print(f"2nd place: {winners_list[1][0]}")
print(f"3rd place: {winners_list[2][0]}")