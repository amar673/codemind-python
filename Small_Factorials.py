for _ in range(int(input())):
    a=int(input())
    fa=1
    for i in range(1,a+1):
        fa*=i
    print(fa)