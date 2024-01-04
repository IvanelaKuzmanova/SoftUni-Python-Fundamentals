number_of_snowballs = int(input())

highest_value = 0
highest_quality = 0
highest_weight = 0
time = 0

for ball in range(number_of_snowballs):

    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    current_ball_value = (weight / time_to_target) ** quality

    if current_ball_value > highest_value:
        highest_value = int(current_ball_value)
        highest_quality = quality
        highest_weight = weight
        time = time_to_target

print(f"{highest_weight} : {time} = {highest_value} ({highest_quality :.0f})")
