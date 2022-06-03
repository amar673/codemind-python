a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
h=0
for i in set(l1):
    if i not in set(l2):
        h+=1
for i in set(l2):
    if i not in set(l1):
        h+=1
print(h)
            