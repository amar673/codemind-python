a,b=map(int,input().split())
if a<b:
    a,b=b,a
if b+1==a or a-b==9:
    print("Yes")
else:
    print("No")