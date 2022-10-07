a=int(input())
l=list(map(int,input().split()))
b=[]
c=0
for i in l:
    if l.count(i)==1:
        b.append(i)
    else:
        c+=1
if c<a:
    print(max(b))
else:
    print(-1)