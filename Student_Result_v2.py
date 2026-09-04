No=int(input("Enter the number of students: "))
students=[]
for i in range(No):
    name=input("Enter the name of student: ")
    student={}
    student['name']=name
    students.append(student)
    
sub = int(input("Enter number of subjects: "))
marks = []
for i in range(sub):
    mark = int(input("Enter mark: "))
    marks.append(mark)
