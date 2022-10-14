s=input()
s=s.lower()
s=s.split()
m=s[0]
l=[]
for i in m:
    c=0
    for j in range(len(s)):
        if i in s[j]:
            c+=1
    if c==len(s):
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(min(l))