l=list(map(str,input().split()))
c=[]
d=0
for i in range(len(l)):
    if i%2==0:
        d=l[i][::-1]
        c.append(d)
    else:
        c.append(l[i])
print(*c)