import math
def prime(a):
    if a<=1:
        return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1

a=int(input())
c=1
if prime(a):
    while(a):
        b=a%10
        if prime(b)==0:
            c=0
            break
        a=a//10
    if c==0:
        print("Not Mega Prime")
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")