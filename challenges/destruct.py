# x, y = 5, 11

student_attendance = {"Sue": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))
# gives a list of tuples
# [('Sue', 96), ('Bob', 80), ('Anne', 100)]

for t in student_attendance.items():
    print(t)

    # destructured into students and grades:
    for student, attendance in student_attendance.items():
        print(f"{student}: {attendance}")
