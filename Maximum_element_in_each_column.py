a,b=map(int,input().split())
l=[]
for i in range(a):
    x=list(map(int,input().split()))
    l.append(x)
for i in range(a):
    c=0
    for j in range(b):
        if c<l[j][i]:
            c=l[j][i]
    print(c)