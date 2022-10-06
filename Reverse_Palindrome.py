def rev(a):
    b=str(a)
    return int(b[::-1])
    
a=int(input())
while (1):
    b=rev(a)
    c=a+b
    if rev(c)==c:
        print(c)
        break
    else:
        a=c