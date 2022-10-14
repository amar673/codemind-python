n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
s=0
for i in range(m):
    k=0
    for j in range(n):
        k+=l[j][i]
    if k>s:
        s=k
print(s)