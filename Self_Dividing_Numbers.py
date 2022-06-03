def rev(a):
    temp=a
    while a:
        c=a%10
        a=a//10
        if c==0 or temp%c!=0:
            return 0
    if a==0:
        return 1
        
n=int(input())
m=int(input())
for i in range(n,m+1):
    if rev(i):
        print(i,end="")
    