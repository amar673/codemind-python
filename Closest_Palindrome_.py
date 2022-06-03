def rev(a):
    b=str(a)
    i=b[::-1]
    if b==i:
        return 1
    else:
        return 0
n=int(input())
i=n
#print(n)
j=n
co=0
v=0
while True:
    i-=1
    j+=1
    co+=1
    if rev(i):
        break
    if rev(j):
        v=1
        break
if v==0:
    if rev(j):
        print(i,j)
    else:
        print(i)
else:
    print(j)
    
        
        