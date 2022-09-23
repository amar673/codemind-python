s=input()
k=len(s)
s=s.split()
v0="aeiou"
for i in s:
    c=0
    for j in i:
        if j in v0:
            c+=1
    if c<k:
        k=c
print(k)
    
    
