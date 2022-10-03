def isprime(a):
    if a<=1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True

a=int(input())
l,m=0,0
c=0
for i in range (1,a//2):
    for j in range(i+1,a):
        if i*j==a:
            if isprime(i) and isprime(j): 
                l,m=i,j
                c+=1
                break
if c==1:
    print(l,m)
else:
    print(-1)