s=input()
s1="AEIOUaeiou"
v=0
d=0
w=0
for i in s:
    if i==" ":
        w+=1
    elif i.isdigit():
        d+=1
    elif i in s1:
        v+=1
print("Vowels:",v)
print("Consonants:",len(s)-v-d-w)
print("Digits:",d)
print("White spaces:",w)