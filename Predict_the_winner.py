n=int(input())
e=0
o=0
l=list(map(int,input().split()))
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if abs(e-o)%4==0:
    print('X')
else:
    print('Y')