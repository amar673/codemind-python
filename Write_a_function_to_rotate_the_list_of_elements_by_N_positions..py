a=int(input())
l=list(map(int,input().split()))
b=int(input())
for i in range(b):
    l.insert(0,l[-1])
    l.pop()
print(*l)