s=input()
c=0
for i in s:
    if i.isdigit() or i.isupper() or i.islower() or i==" ":
        continue
    else:
        c+=1
print(c)