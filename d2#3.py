#3 write a function: def table(num): that prints the multiplication table of a number.
def table(num):

    for i in range(1,11):
        print(num,"*",i,"=",i*num)
table(4)
