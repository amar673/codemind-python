def prime(a):
    if a<=1:
        return 0
    for i in range(2,a):
        if a%i==0:
            return(0)
    return 1
a=int(input())
if prime(a):
    print("prime")
else:
    print('not a prime')
