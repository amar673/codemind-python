n=int(input())
a=abs(n)
temp=a
rev=0
while temp:
    s=temp%10
    temp=temp//10
    rev=(rev*10)+s
if n<0:
    print(-rev)
else:
    print(rev)
    
    