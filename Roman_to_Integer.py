s=input()
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
sum=d[s[-1]]
for i in range(len(s)-1):
    m=s[i]
    if d[m]<d[s[i+1]]:
            sum-=d[s[i]]
    else:
        sum+=d[s[i]]
print(sum)
