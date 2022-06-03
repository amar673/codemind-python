a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
h=[]
for i in l1:
    if i not in l2:
        if i not in h:
            h.append(i)
for i in l2:
    if i not in l1:
        if i not in h:
            h.append(i)
print(*h)
            