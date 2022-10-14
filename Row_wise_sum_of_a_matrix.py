n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ev=od=0
for i in l:
    print(sum(i),end=" ")