l=list(map(str,input().split()))
c=[]
b=0
for i in range(len(l)):
    b=l[i][::-1]
    c.append(b)
print(*c)