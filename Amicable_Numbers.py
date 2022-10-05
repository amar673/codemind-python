def factors(a):
    a1=0
    for i in range(1,a):
        if a%i==0:
            #print(i)
            a1+=i
    return a1
    
a=int(input())
b=int(input())
a1=factors(a)
b1=factors(b)
#print(a,b,a1,b1)
if b1==a and b==a1:
    print("Amicable")
else:
    print("Not Amicable")