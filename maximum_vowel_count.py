s=input()
s=s.split()
v0="aeiouAEIOU"
k=0
for i in s:
    c=0
    for j in i:
        if j in v0:
            c+=1
    if k<c:
        k=c
print(k)
    
    
