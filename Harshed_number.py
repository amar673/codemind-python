n=int(input())
temp=n
s=0
while temp:
    b=temp%10
    temp=temp//10
    s+=b
if n%s==0:
    print(True)
else:
    print(False)
    