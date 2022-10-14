n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(m):
    s=0
    for j in range(n):
        s+=l[j][i]
    print(s,end=" ")