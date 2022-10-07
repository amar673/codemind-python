a=int(input())
l=list(map(int,input().split()))
a2=int(input())
l2=list(map(int,input().split()))
c=0
c=1
if a==a2:
    l.sort()
    l2.sort()
    if l==l2:
        print(True)
    else:
        print(False)
else:
    print(False)
    