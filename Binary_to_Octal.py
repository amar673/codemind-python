n=int(input())
for kk in range(n):
    s=input()
    if len(s)%3!=0:
        for i in range(3-len(s)%3):
            s='0'+s
    k=""
    for i in range(0,len(s),3):
        k+=str(int(s[i:i+3],2))
    if k[0]=='0':
        print(k[1:])
    else:
        print(k)