name=input("Enter your name: ")
print("Student Name:",name)
A=int(input("Enter the no of subjects:"))
print("Enter the marks of",A,"subjects:")
marks = []
for i in range(A):
    mark = int(input("Enter mark: "))

    while mark < 0 or mark > 100:
        print("Invalid mark. Enter again!")
        mark = int(input("Enter mark: "))

    marks.append(mark)
def calculate_total(marks):
    total=0
    for mark in marks:
        total+=mark
    return total
def calculate_average(marks):
    total=calculate_total(marks)
    average=total/len(marks)
    return average
def get_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"
def check_result(average):
    if average>=60:
        return "Pass"
    else:
        return "Fail"
def highest_mark(marks):
    highest=marks[0]
    for mark in marks:
        if mark>highest:
            highest=mark
    return highest
total=calculate_total(marks)
average=calculate_average(marks)
grade=get_grade(average)
result=check_result(average)
highest=highest_mark(marks)
print("Total Marks:",total)
print("Average Marks:",average)
print("Grade:",grade)
print("Result:",result)
print("Highest Mark:",highest)