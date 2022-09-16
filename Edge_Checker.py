a,b=map(int,input().split())
if a<b:
    a,b=b,a
if a-1==b or a-b==9:
    print("Yes")
else:
    print("No")