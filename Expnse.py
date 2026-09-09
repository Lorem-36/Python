expenses=[]
no_of_expense=int(input("Enter the no of expense:"))

for i in range(no_of_expense):
    name=input("Name: ")
    amount=int(input("Amount: "))
    category=input("Category: ")
    expense= {
     "name":name,
     "amount":amount,
     "category":category 
     }
    expenses.append(expense)

print("List of Expenses",expenses)
def calculate_total(expenses):
     total=0
     for i in expenses:
         total=total+i["amount"]
     return total
result=calculate_total(expenses)
print("Total:",result)

def category_total(expenses, category):
    total=0
    for i in expenses:
        if i["category"] == category:
            total=total+i["amount"]
    return total
category=input("Enter the category to calculate:")
result = category_total(expenses, category)
print("Food Expense:", result)