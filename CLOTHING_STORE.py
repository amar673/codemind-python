n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i not in b:
        if l.count(i)%2:
            a.append(l.count(i)-1)
        else:
            a.append(l.count(i))
        b.append(i)
s=sum(a)
print(s//2)
