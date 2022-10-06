a=int(input())
b=a*a
a1=str(a)
b1=str(b)
l1=len(a1)
b2=b1[l1::]
if int(b2)==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")