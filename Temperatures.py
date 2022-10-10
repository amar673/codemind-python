n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    c=0
    for j in range(i+1,len(l)):
        c+=1
        if l[i]<l[j]:
            print(c,end=" ")
            break
    else:
        print(0,end=" ")