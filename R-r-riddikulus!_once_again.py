a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b%a):
    l.append(l.pop(0))
print(*l)
