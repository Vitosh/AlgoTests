students_number = int(input())
list_students = []

for i in range(0, students_number):
    list_students.append(input())

days = int(input())
present_students = []
for days in range(0, days):
    students_number = int(input())
    current_students = []
    for student in range(0,students_number):
        current_students.append(input())
    present_students.append(current_students)

result_array = []
for day in present_students:
    small_result = []
    for student in list_students:
        if not student in day:
            small_result.append(student)
    small_result.sort()
    result_array.append(small_result)

print(result_array)