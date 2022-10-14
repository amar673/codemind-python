s=input()
s=s.lower()
s=s.split()
c=""
for i in range(len(s[0])):
    k=s[0][i]
    cc=0
    for j in s:
        if k in j:
            cc+=1
    if cc==len(s):
        c+=k
if len(c)==0:
    print(-1)
else:
    print(c)