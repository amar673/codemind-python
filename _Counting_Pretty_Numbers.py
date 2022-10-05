for _ in range(int(input())):
    i,b=map(int,input().split())
    co=0
    for a in range(i,b+1):
        if a%10==2 or a%10==3 or a%10==9:
            co+=1
    print(co)