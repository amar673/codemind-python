def palin(a):
    b=str(a)
    if a==int(b[::-1]):
        return 1
    return 0
 
 
a=int(input())
b=int(input())
for i in range(a,b+1):
    if palin(i):
        print(i,end=" ")