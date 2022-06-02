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
b=a+1
co=0
for i in range (1,b):
    if a%i==0:
        if prime(i)==0:
            co+=1
print(co)
