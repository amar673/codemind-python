t=int(input())
for i in range(t):
    deci=0
    s=input()
    s=list(s)
    #print(s)
    s=s[::-1]
    for i in range(len(s)):
        #print(s[i],deci)
        deci+=(2**i)*int(s[i])
    print(deci)
    