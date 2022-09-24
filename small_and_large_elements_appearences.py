s=input()
s=list(s)
f=[]
for i in range(len(s)):
    if s[i]!=" ":
        f.append(s[i])
print(min(f),f.count(min(f)),max(f),f.count(max(f)))        