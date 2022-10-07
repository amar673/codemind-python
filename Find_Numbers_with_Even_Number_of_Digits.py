_=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    a=str(i)
    if len(a)%2==0:
        c+=1
print(c)