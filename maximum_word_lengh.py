l=list(map(str,input().split()))
b=[]
c=0
for i in l:
    c=len(i)
    b.append(c)
print(max(b))