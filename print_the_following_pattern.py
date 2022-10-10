n=int(input())
for i in range(n):
    for j in range(n):
        print(chr(64+i+1),end=" ")
    print()