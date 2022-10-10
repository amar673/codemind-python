a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
k=0
for i in range(a):
    if l[i]<=b:
        c+=1
    else:
        k+=1
    if k==2:
        break
print(c)
