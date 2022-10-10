t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in l:
        if j&1:
            c+=1
    if sum(l)&1:
        print((c-1)//2)
    else:
        print(c//2)
