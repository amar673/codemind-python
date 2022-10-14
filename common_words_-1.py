
s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.split()
s1=s1.split()
c=0
for i in s1:
    if i in s:
        c+=1
if c==0:
    print(-1)
else:
    print(c)
