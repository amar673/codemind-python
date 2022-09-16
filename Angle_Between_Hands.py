a=input()
a=a.split(":")
a=list(a)
g=(int(a[0])*60+int(a[1])) *0.5
min=int(a[1])*6
ans=abs(g-min)
if ans>180:
    ans=360-ans
print(ans)

