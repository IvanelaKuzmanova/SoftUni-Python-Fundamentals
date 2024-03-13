courses = {}

while True:

    command = input().split(" : ")

    if command[0] == "end":
        break

    course_name = command[0]
    student_name = command[1]

    if course_name not in courses.keys():
        courses[course_name] = []

    courses[course_name].append(student_name)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")