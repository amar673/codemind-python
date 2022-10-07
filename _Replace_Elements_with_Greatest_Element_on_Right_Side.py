n=int(input())
l=list(map(int,input().split()))
c=[]
for  i in range(n-1):
    e=max(l[i+1:])
    c.append(e)
for j in range(n):
    if len(c)!=n:
        c.append(-1)
print(*c)