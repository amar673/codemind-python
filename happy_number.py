def rev(a):
    d=0
    while(a):
        b=a%10
        a=a//10
        c=b*b
        d+=c
        #print(d)
    return d
        
a=int(input())
#print(a)
while(a>=10):
    a=rev(a)
    #print(a)
if a==1 or a==7:
    print(True)
else:
    print(False)
