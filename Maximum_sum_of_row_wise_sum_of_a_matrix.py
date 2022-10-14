n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
s=sum(l[0])
for i in range(n):
    if sum(l[i])>s:
        s=sum(l[i])
print(s)