s=input()
s=s.split()
for i in range(len(s)//2):
    s[i],s[-1-i]=s[-1-i],s[i]
print(" ".join(s))
