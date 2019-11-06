def sol2():
    for x in range (1,51):
        if count1s(x)%2==1:
            print(x)


def count1s(num):
    count=0
    while num!=0:
        q=num%2
        if q==1:
            count+=1
        num=num/2
    return count

sol2()


    


