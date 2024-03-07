people_dict = {}

while True:

    command = input()

    if command.islower() or ("_" in command):
        course_name = command
        break

    name, id, course = command.split(":")          #taking three separate values at once instead of iterating through list
    snakecase_course = "_".join(course.split())

    if snakecase_course not in people_dict:
        people_dict[snakecase_course] = []          #if not already in, we add another key with value empty list

    people_dict[snakecase_course].append((name, id))        #adding tuples with peoples names and id to the correspoding course if they have interest in it

result = []

for s_name, s_id in people_dict[course_name]:       #taking and printing all participants in the given course name!!!
    result.append(f'{s_name} - {s_id}')

print('\n'.join(result))

#keys in the dict are the courses, and their values are lists of tuples for each person attending the course