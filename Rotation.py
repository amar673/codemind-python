t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(b):
        l.insert(0,l[-1])
        l.pop()
    print(*l)