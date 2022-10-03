a=int(input())
for i in range(a):
    for j in range(a):
        if j==i:
            print(0,end="")
        else:
            print('x',end="")
    print()
    