n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i&1:
        l2.append(i)
    else:
        l1.append(i)
if len(l1)<len(l2):
    for i in range(len(l1)):
        print(l2[i],l1[i],end=" ")
    if (len(l1)+len(l2))&1:
        l2.append(0)
    print(*l2[len(l1):])
elif len(l1)>len(l2):
    for i in range(len(l2)):
        print(l2[i],l1[i],end=" ")
    if (len(l1)+len(l2))&1:
        l1.append(0)
    print(*l1[len(l2):])
else:
    for i in range(len(l1)):
        print(l2[i],l1[i],end=" ")