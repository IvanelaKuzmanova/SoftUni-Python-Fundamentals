initial_energy = 100
initial_coins = 100

events_as_string = input().split("|")       #creating full list of all commands

for command in range(len(events_as_string)):

    command_as_list = events_as_string[command].split("-")          #in each iteration separating each command to list of separate components

    # if "rest" in events_as_string[command]:

