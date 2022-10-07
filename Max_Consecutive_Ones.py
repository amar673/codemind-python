a=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in l:
    if i==1:
        d+=1
    else:
        d=0
    if c<d:
        c=d
print(c)
    