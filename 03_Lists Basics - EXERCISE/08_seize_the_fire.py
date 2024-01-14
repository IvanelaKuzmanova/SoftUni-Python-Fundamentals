commands_as_list = input().split("#")
water_amount = int(input())

fire_types_list = []
value_of_cells_list = []

for element in commands_as_list:
    command_separated = element.split("=")
    fire_type = command_separated[0]
    water_needed = command_separated[1]

    # for i in range(len(element)):
    #     fire_types_list.append(i[0])
    #     value_of_cells_list.append(i[2])
#
#
#
#

#
#
#
# print(commands_as_list)