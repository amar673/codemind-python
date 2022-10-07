a=input()
c=1
for i in range(1,len(a)-1):
    if a[i].isupper():
        c+=1
print(c)