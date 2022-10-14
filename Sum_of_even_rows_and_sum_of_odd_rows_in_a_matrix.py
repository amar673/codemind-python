n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ev=od=0
for i in range(len(l)):
    if i&1:
        od+=sum(l[i])
    else:
        ev+=sum(l[i])
print(ev,od)