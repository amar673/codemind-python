def palin(a):
    e=str(a)
    b,d,rev=0,0,0
    c=10**(len(e)-1)
    while a:
        b=a%10
        a=a//10
        d=b*c
        c=c//10
        rev+=d
    return rev
a=int(input())
b=list(map(int,input().split()))
c=0
d=0
e=[]
for i in b:
    d=palin(i)
    e.append(d)
print(*e)