_=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(len(l)):
    c=0
    for j in range(0,len(l)):
        if l[i]>l[j]:
            c+=1
    b.append(c)
print(*b)
        
        