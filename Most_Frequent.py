a=int(input())
l=list(map(int,input().split()))
a=set(l)
c=0
for i in a:
    if l.count(i)>c:
        c=l.count(i)
        b=i
print(b)