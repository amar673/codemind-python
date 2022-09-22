def sodd(b):
    c=len(b)
    d=0
    e=0
    for i in range(1,c):
        if b[i]%2 and i%2:
            d+=1
        if b[i]%2:
            e+=1
    if d==e:
        return True
    return False


a=int(input())
l=list(map(int,input().split()))
if sodd(l):
    print("True")
else:
    print(False)