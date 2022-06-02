def prime(a):
    co=0
    for i in range(1,a):
        if a%i==0:
            co+=1
    if co==1:
        return 1
    else:
        return 0

def palind(a):
    b=str(a)
    c=b[::-1]
    if c==b:
        return 1
    else:
        return 0
        
a=int(input())
b=str(a)
b=b[::-1]
c=int(b)
if prime(a):
    if prime(a) and prime(c):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")

    
