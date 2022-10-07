n,k=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
#print(a)
for i in range(len(a)+1):
    for j in range(i):
        if sum(a[j:i])==k:
            cnt+=1
print(cnt)