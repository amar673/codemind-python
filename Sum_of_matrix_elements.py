a=int(input())
b=int(input())
c=[]
for i in range(a):
    l=list(map(int,input().split()))
    c.append(l)
c1=0
for i in range(a):
    for j in range(b):
        c1+=c[i][j]
print(c1)
        