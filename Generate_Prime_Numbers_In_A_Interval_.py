def prime(a):
    co=0
    for i in range(1,a):
        if a%i==0:
            co+=1
    if co==1:
        return 1
    else:
        return 0
        
a=int(input())
b=int(input())
#print(a,b)
for i in range (a,b):
    if prime(i):
        print(i)
