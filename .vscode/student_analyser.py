#Mini Project: Student Grade Manager
name = input("Enter the Name of student: ")
sub = int(input("Enter the no. of subject: "))
marks = []

for i in range(sub):
    mark = int(input("Enter the subject Marks: "))
    marks.append(mark)


def calculate_total(marks):
    total = 0
    for i in marks:
        total = total + i
    return total

a1 = calculate_total(marks)
print("Student:", name)
print("Total Marks:", a1)

def calculate_average(marks, a1):
    average = a1 / len(marks)
    return average
a2 = calculate_average(marks, a1)
print("Average:", a2)


def get_grade(a2):
    if a2 >= 90:
        return "A"
    elif a2 >= 75:
        return "B"
    elif a2 >= 60:
        return "C"
    elif a2 >= 40:
        return "D"
    else:
        return "F"

a3 = get_grade(a2)
print("Grade:", a3)