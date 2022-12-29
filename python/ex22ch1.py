n=int(input('enter the no. :'))
a=0
b=1
tup=()
for i in range(0,n):
    tup=tup+(a,)
    c=a+b
    a=b
    b=c
    print(tup)
    
    
    
