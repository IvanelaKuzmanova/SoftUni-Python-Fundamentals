number_of_rooms = int(input())
total_visitors = 0
total_chairs = 0

for room in range(1, number_of_rooms + 1):

    current_information = [x for x in input()]

    for element in current_information:
        if element.isdigit():
            current_people = int(element)
            total_visitors += current_people

    current_chairs = current_information.count('X')
    total_chairs += current_chairs

    if current_chairs < current_people:
        chairs_needed = current_people - current_chairs
        print(f"{chairs_needed} more chairs needed in room {room}")

if total_chairs >= total_visitors:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")
