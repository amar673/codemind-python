n=int(input())
for _ in range(int(input())):
    a,b=map(int,input().split())
    #print(a,b)
    if a<n or b<n:
        print("UPLOAD ANOTHER")
    elif a==b:
        print("ACCEPTED")
    else:
        print("CROP IT")