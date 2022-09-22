l=list(map(str,input().split()))
b=str(l)
c=l[::-1]
d=[]
e=0
for i in range(len(c)):
    e=c[i][::-1]
    d.append(e)
print(*d)