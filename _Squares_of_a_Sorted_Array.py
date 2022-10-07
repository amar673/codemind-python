a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    b.append(i*i)
b.sort()
print(*b)