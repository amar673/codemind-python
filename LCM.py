def gcd(a,b):
    if a>b:
        a,b=b,a
    while(a):
        b=b%a
        if a>b:
            a,b=b,a
    return b

a,b=map(int,input().split())
lcm=a*b
d=gcd(a,b)
print(lcm//d)