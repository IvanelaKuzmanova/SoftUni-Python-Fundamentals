import math


def point_check(point1_x:float, point1_y:float, point2_x:float, point2_y:float,
                point3_x:float, point3_y:float, point4_x:float, point4_y:float) -> str:

    sum_1 = abs(point1_x) + abs(point1_y)
    sum_2 = abs(point2_x) + abs(point2_y)
    sum_3 = abs(point3_x) + abs(point3_y)
    sum_4 = abs(point4_x) + abs(point4_y)

    sums_list = [sum_1, sum_2, sum_3, sum_4]
    longest_list_sums = []

    for sums in range(len(sums_list)):
        longest = max(sums_list)
        longest_list_sums.append(longest)
        sums_list.remove(longest)
        if len(longest_list_sums) == 2:
            break

    longest_list_sums = longest_list_sums[::-1]
    longest_points_coordinates = []

    for sum in longest_list_sums:
        if sum == sum_1:
            longest_points_coordinates.append(point1_x)
            longest_points_coordinates.append(point1_y)
        elif sum == sum_2:
            longest_points_coordinates.append(point2_x)
            longest_points_coordinates.append(point2_y)
        elif sum == sum_3:
            longest_points_coordinates.append(point3_x)
            longest_points_coordinates.append(point3_y)
        elif sum == sum_4:
            longest_points_coordinates.append(point4_x)
            longest_points_coordinates.append(point4_y)

    if abs(longest_list_sums[0]) == abs(longest_list_sums[1]):
        return f"({int(longest_points_coordinates[0])}, {int(longest_points_coordinates[1])})"
    else:
        return f"({int(longest_points_coordinates[0])}, {int(longest_points_coordinates[1])})({int(longest_points_coordinates[2])}, {int(longest_points_coordinates[3])})"

    #aко са еднакви отрицателни
    #aко са еднакви положителни
    #ако са различни отрицателни
    #ако са различни положителни


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


result = point_check(x1, y1, x2, y2, x3, y3, x4, y4)

print(result)


