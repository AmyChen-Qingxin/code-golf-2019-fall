x,y=input().split();ansx='';ansy=''
if(x[0]=='-'):ansx='-'+x[1:][::-1];x=-float(x[1:][::-1])
else: ansx=x[::-1];x=float(ansx)
if(y[0]=='-'):ansy='-'+y[1:][::-1];y=-float(y[1:][::-1])
else: ansy=y[::-1];y=float(ansy)
if(x>=y):print(ansx)
#elif(x>=y):print(x)
else: print(ansy)