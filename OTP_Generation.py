def otp(a):
    rev=0
    a1=[]
    while(a):
        b=a%10
        a=a//10
        if b%2:
            b=b*b
            a1.append(b)
    return a1
    
n=int(input())
a=otp(n)
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")
        