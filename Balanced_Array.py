t=int(input())
for _ in range(t):
    l=int(input())
    n=list(map(int,input().split()))
    k=sum(n)
    m=0
    for i in range(len(n)):
        if m==k-n[i]-m:
            print("YES")
            break
        else:
            m+=n[i]
    else:
        print("NO")
