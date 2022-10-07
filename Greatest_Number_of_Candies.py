_=int(input())
l=list(map(int,input().split()))
a=int(input())
b=[]
for i in l:
    if i+a>=max(l):
        b.append(True)
    else:
        b.append(False)
print(*b)
