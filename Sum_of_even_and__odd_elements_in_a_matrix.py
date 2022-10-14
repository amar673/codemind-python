n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ev=od=0
for i in l:
    for j in i:
        if j&1:
            od+=j
        else:
            ev+=j
print(ev,od)