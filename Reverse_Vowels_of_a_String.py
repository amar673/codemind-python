s=input()
i=0
s=list(s)
j=len(s)-1
s1="AEIOUaeiou"
while i<=j:
    if s[i] in s1:
        if s[j] in s1:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        else:
            j-=1
    else:
        i+=1
print("".join(s))