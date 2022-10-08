n=int(input())
l=list(map(int,input().split()))
n=int(input())
c=0
for i in range(len(l)):
    if l[i]==n:
        print(i)
        c=1
        break
if c==0:
    print(-1)