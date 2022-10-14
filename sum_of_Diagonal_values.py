n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
s=0
if len(l)==1:
    print(l[0][0])
else:
    for i in range(n):
        s+=l[i][i]
        s+=l[i][-i-1]
    if n%2:
        s-=l[n//2][n//2]
    print(s)