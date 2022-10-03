def isprime(a):
    if a<=1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1

a=int(input())
b=int(input())
c=0
while c<=a+b:
    c+=1
    if isprime(c+a+b):
        print(c)
        break