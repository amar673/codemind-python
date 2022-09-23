s=input()
s=s.split()
l=[]
c1=0
v="aeiouAEIOU"
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
for i in l:
    if i==max(l):
        c1+=1
print(c1)