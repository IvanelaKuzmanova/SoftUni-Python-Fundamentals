pairs_number = int(input())
student_grades = {}
kept_students = {}

for pair in range(pairs_number):

    name = input()
    grade = float(input())

    if name not in student_grades.keys():
        student_grades[name] = []

    student_grades[name].append(grade)

for student, grade in student_grades.items():

    average_grade = sum(grade) / len(grade)
    student_grades[student] = average_grade

    if average_grade >= 4.50:
        kept_students[student] = average_grade

for key, value in kept_students.items():
    print(f"{key} -> {value:.2f}")
