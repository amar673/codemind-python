s=input()
s1=input()
s=s.lower()
s1=s1.lower()
s=s.replace(" ","")
s1=s1.replace(" ","")
s=set(s)
s1=set(s1)
c=0
for i in s:
    if i  not in s1:
        c+=1
for i in s1:
    if i not in s:
        c+=1
print(c)