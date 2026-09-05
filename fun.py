#This is a simple program to calculate the total after discount using nested function.
def cal(num1,num2):
    add=num1+num2
    def dis(add):
        result=add*(10/100)
        total=add-result
        return total
    return dis(add)
res=cal(100,600)
print(res)

#Using function to calculate total and discount separately
def calculate_total(n1,n2):
    total=n1+n2 
    return total
def apply_discount(total):
    discount=total*(10/100)
    final=total-discount
    return final

total = calculate_total(100, 600)
final_total = apply_discount(total)
print(final_total)

#Using function to calculate total and discount separately with user input
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
d1=int(input("Enter the discount percentage:"))
def cal(n1,n2):
    total=n1+n2
    return total
cal(n1,n2)
def dis(total,d1):
    discount=total*(d1/100)
    final=total-discount
    return final
fun=dis(cal(n1,n2))

print("The final total after discount is:",fun)
#Using function to calculate total and discount separately with user input
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
d1 = int(input("Enter the discount percentage: "))


def cal(n1, n2):
    total = n1 + n2
    return total


def dis(total, d1):
    discount = total * (d1 / 100)
    final = total - discount
    return final


total = cal(n1, n2)

fun = dis(total, d1)

print("The final total after discount is:", fun)