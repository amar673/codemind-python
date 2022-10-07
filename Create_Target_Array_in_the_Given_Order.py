_=int(input())
l=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
c=[]
for i in range(b):
    c.insert(l2[i],l[i])
print(*c)