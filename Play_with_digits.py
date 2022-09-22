def play(a):
    b,c=0,0
    while a:
        b=a%10
        a=a//10
        c+=b
    return c
a=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=play(i)
print(s)