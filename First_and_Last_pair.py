n=int(input())
l=list(map(int,input().split()))
m=[]
k=[]
if n%2!=0:
    for i in range((n//2)+1):
        m.append(l[i])
    for j in range(n-1,n//2,-1):
        k.append(l[j])
    k.append(0)
    for g in range(len(k)):
        print(m[g],k[g],end=" ")
else:
    for i in range(0,n//2):
        m.append(l[i])
    for j in range(n-1,(n//2)-1,-1):
        k.append(l[j])
    for g in range(len(k)):
        print(m[g],k[g],end=" ")