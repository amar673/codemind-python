n=int(input())
l=list(map(int,input().split()))
if n<=2:
    print("no")
else:
    for i in range(2,n):
        if l[i-2]+l[i-1]!=l[i]:
            print("no")
            break
    else:
        print("yes")