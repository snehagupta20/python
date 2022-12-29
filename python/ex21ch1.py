n=int(input("enter the no. of elemnts of the list"))
l=[]
for i in range(n):
    n1=int(input("enter the integer element"))
    l.append(n1)
print("your list is",l,)
print("max",max(l),"min",min(l),"avg",sum(l)/len(l))
    
