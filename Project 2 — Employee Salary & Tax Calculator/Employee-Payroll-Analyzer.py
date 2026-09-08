#Mini-Project 2 — Employee Salary & Tax Calculator
name=input("Enter the employee Name:")
salary=int(input("Enter your salary:"))
bonus=int(input("Enter your bonus percentage: "))
tax_percentage=int(input("Enter tax percentage: "))
def calculate_bonus(salary,bonus):
    final=(salary*bonus)/100
    final=final+salary
    return final

def check_tax(final,tax_percentage):
    total = (final * tax_percentage) / 100
    total=final-total
    return total

def check_salary(total):
    if total>=100000:
        print("You are in the highest salary bracket")
    elif total>=50000:
        print("You are in the middle salary bracket")
    else:
        print("You are in the lowest salary bracket")
        
print("Employee Name:",name)
result=calculate_bonus(salary,bonus)
print("Your total before tax with bonus is:",result)
total=check_tax(result,tax_percentage)
print("Your total after tax with bonus is:",total)
check_salary(total)