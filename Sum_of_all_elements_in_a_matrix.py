n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
s=0
for i in l:
    s+=sum(i)
print(s)