s=input()
s=s.lower()
s=s.split()
c=0
for i in range(len(s[0])):
    k=s[0][i]
    cc=0
    for j in s:
        if k in j:
            cc+=1
    if cc==len(s):
        c+=1
print(c)