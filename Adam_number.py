def rev(a):
    b=str(a)
    i=b[::-1]
    return int(i)
def square(a):
    a=a*a
    return a

n=int(input())
sqofn=square(n)
revofn=rev(n)
sqofrevofn=square(revofn)
out=rev(sqofrevofn)
if out==sqofn:
    print(True)
else:
    print(False)
    
        
        