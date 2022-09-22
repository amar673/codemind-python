a=int(input())
b=list(map(str,input().split()))
c=[]
for i in b:
    c1=len(i)
    c+=[c1]
m=min(c)
coun=c.count(m)
print(coun)