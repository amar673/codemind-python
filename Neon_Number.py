a=int(input())
sq=a*a
temp=sq
ans=0
while(temp):
    rem=temp%10
    temp=temp//10
    ans+=rem
if ans==a:
    print("Neon Number")
else:
    print("Not Neon Number")