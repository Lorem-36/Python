#Using functions to calculate shopping bill
a=int(input("Enter the no. of items: "))
prices=[]
for i in range(a):
    a1=int(input("Enter price: "))
    prices.append(a1)
print(prices)
def calculate_total(prices):
    total=0
    for price in prices:
        total+=price
    return total
total=calculate_total(prices)
print("Total price:",total)
d1=int(input("Enter the discount percentage: "))
def apply_discount(total,d1):
    discount=total*(d1/100)
    total=total-discount
    return total
final=apply_discount(total,d1)
print("Final price after discount:",final)
