def adam(a):
    tem=a
    d=0
    s=str(a)
    i=len(s)
    while a:
        c=a%10
        a=a//10
        d+=c**i
        i-=1
        #print(d,c,a)
    if tem==d:
        return 1
    else:
        return 0
a=int(input())
#print(a)
if adam(a):
    print(True)
else:
    print(False)
    