l,r,k=map(int,input().split())
co=0
for i in range(l,r+1):
    if i%k==0:
        co+=1
print(co)