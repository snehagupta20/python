l=[12,13,14,1,523,24,34,43,12,13,13,14,1]
l1=[]
l2=[]
for i in l:
    x=l.count(i)
    if x>1:
        l1.append(i)
    elif x==1:
        l2.append(i)
print("unique:",l2)
print("dublicate:",l1)
