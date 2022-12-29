n=input("enter a string")
K=0
j=0
for i in n:
    if i.isupper():
        K=K+1
    else:
        j=j+1
print("no. of upper case:",K,'no. of lower case',j)        
