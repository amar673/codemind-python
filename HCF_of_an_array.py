def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        else:
            b=b%a
    return a
n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    l[i+1]=gcd(l[i],l[i+1])
print(l[-1])