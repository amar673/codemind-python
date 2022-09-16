t=int(input())
for i in range(t):
    a=int(input())
    l=list(map(int,input().split()))
    b=[]
    for i in l:
        b.append(i)
    l.sort()
    if l==b:
        print(0)
    else:
        print(max(l)-min(l))
    
    