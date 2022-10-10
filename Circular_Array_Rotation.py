a,b,c=map(int,input().split())
l=list(map(int,input().split()))
for j in range(b%a):
    l.insert(0,l.pop())
for i in range(c):
    print(l[int(input())])
