#to learn how to taken input and print output, use of if,else
a=input("Enter the Name:")
print("hello ",a," Welcome to Python")
b=int(input("Enter your Age:"))
print("You are ",b," year old")
if b>=18:
    print("You is eligible to have license Thank you")

elif b>=70:
     print("Sorry you is too old to have license")
else:
    print("Sorry! try another year")
    