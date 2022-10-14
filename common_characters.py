s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.replace(" ","")
s1=s1.replace(" ","")
s=set(s)
s1=set(s1)
c=""
for i in s:
    if i in s1:
        c+=i
c=sorted(c)
c="".join(c)
if len(c)==0:
    print(-1)
else:
    print(c)