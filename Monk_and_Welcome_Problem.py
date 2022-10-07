t=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=[]
for i in range(t):
    c.append(l1[i]+l2[i])
print(*c)