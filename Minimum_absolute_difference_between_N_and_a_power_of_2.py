n=int(input())
k=n
m=n
while True:
    if m&(m-1)==0:
        c=m
        break
    if n&(n-1)==0:
        c=n
        break
    n+=1
    m-=1
print(abs(c-k))