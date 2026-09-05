salary=int(input("Enter your salary:"))
bonus=int(input("Enter your bonus percentage: "))
tax_percentage=int(input("Enter tax percentage: "))
def calculate_bonus(salary,bonus):
    final=(salary*bonus)/100
    final=final+salary
    return final

def tax(final,tax_percentage):
    total = (final * tax_percentage) / 100
    total=final-total
    return total

result=calculate_bonus(salary,bonus)
print("Your total before tax with bonus is:",result)
total=tax(result,tax_percentage)
print("Your total after tax with bonus is:",total)