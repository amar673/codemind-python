def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input())
l=list(map(int,input().split()))
a=l.index(min(l))
b=l.index(max(l))+1
if a>b:
    a,b=b,a
l=l[a:b]
c=0
for i in l:
    if prime(i):
        c+=1
print(c)