a=int(input())
b=list(map(int,input().split()))
for i in range(a-1):
    if b[i]-b[i+1]>=0:
        print("no")
        break
else:
    print("yes")