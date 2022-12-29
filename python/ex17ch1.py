n=int(input("enter the total no. of items"))
n4=0
i=0
while i!=n:
    n1=int(input("enter cost of the item"))
    n2=int(input("enter GST% on the item(only numbers)"))
    n3=(n1*n2/100)+n1
    n4=n4+n3
    i=i+1
print("total cost along with tax is:",n4)
