#Mini Project: Student Grade Manager
name = input("Enter the Name of student: ")
sub = int(input("Enter the no. of subject: "))
list = []

for i in range(sub):
    while True:
        marks = int(input("Enter the subject Marks: "))
        if marks<0 or marks>100:
           print("Invalid Mark, Enter marks btw 0 to 100")
        else:
           break
    list.append(marks)


def calculate_total(list):
    total = 0
    for i in list:
        total = total + i
    return total

a1 = calculate_total(list)
print("Student Name:",name)
print("Total Marks:",a1)

def cal_average(a1,list):
    average=a1/len(list)
    return average
a2= cal_average(a1,list)
print("Average:",a2)

def grade(a2):
    if a2>90:
        return "A"
    elif a2>=75:
        return"B"
    elif a2>=60:
        return "C"
    elif a2>=40:
        return "D"
    else:
        return"Fail"
a3= grade(a2)
print("Grade:",a3)