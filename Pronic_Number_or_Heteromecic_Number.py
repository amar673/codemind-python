n=int(input())
b=1
for i in range(0,n):
    c=i*i+1
    if c==n:
        b=0
        break
if b==0:
    print("NO")
else:
    print("YES")
