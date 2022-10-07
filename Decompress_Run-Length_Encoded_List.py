a=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(0,a,+2):
    for j in range(l[i]):
        c.append(l[i+1])
print(*c)