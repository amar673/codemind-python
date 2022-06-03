n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in range(1,len(l),2):
    for j in range(0,l[i]):
        l2.append(l[i-1])
print(*l2)
    
    