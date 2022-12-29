'''wap to input namesof n countr
ies,capital & currency,store it in
a dictand display in tabular formalso searc
h and display for a particular country'''
n=int(input("enter the no. of countries:"))
dict={}
for i in range(n):
    name=input("enter the name of the country:")
    currency=input("enter the currency")
    capital=input("enter the capital of the country")
    dict[name]=capital,currency
print('name\tcapital and currency')
for i in dict:
    print(i,'\t',dict[i])
