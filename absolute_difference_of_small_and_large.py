s=input().split()
for i in s:
    h=abs(ord(max(i))-ord(min(i)))
    print(h,end=" ")
    