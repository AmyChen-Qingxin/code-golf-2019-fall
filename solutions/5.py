def reverse (num):
    rev = 0
    while(num > 0):r=num%10;rev=rev*10+r;num//=10
    return rev
x,y=input().split()
if(x[0]=='-'):x='-'+x[1:][::-1]
else: x=x[::-1]
if(y[0]=='-'):y='-'+y[1:][::-1]
else: y=y[::-1]
if(x[0]=='-'and y[0]=='-'and x<=y):print(x)
elif(x>=y):print(x)
else: print(y)