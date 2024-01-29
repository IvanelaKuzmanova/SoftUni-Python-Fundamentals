import math


def point_check(point1_x:float, point1_y:float, point2_x:float, point2_y:float) -> str:

    sum_1 = abs(point1_x) + abs(point1_y)
    sum_2 = abs(point2_x) + abs(point2_y)

    closest = min(sum_1, sum_2)

    if closest == 0:
        return f"(0, 0)"

    elif sum_1 == sum_2:
        if sum_1 > 0:
            return f"({math.floor(point1_x)}, {math.floor(point1_y)})"
        elif sum_1 < 0:
            return f"({math.ceil(point1_x)}, {math.ceil(point1_y)})"

    elif closest == sum_1:
        if sum_1 > 0:
            return f"({math.floor(point1_x)}, {math.floor(point1_y)})"
        elif sum_1 < 0:
            return f"({math.ceil(point1_x)}, {math.ceil(point1_y)})"

    elif closest == sum_2:
        if sum_2 > 0:
            return f"({math.floor(point2_x)}, {math.floor(point2_y)})"
        elif sum_2 < 0:
            return f"({math.ceil(point2_x)}, {math.ceil(point2_y)})"


x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

result = point_check(x1, y1, x2, y2)

print(result)


