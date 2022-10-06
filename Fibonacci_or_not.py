n=int(input())
a=(5*n*n +4)
b=(5*n*n -4)
c=int(a**0.5)
d=int(b**0.5)
if c*c==a or d*d==b:
    print(True)
else:
    print(False)
    