s=input()
s=s.split()
a="aeiouAEIOU"
c=0
for i in s:
    
    for j in range(len(i)):
        if ((i[j] in a and i[-j-1] not in a) or (i[j] not in a and i[-j-1] in a)) and i[j]!=" " and i[-j-1]!=" ":
            c+=1
print(c//2)