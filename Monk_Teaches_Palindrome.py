for _ in range(int(input())):
    i=input()
    if i==i[::-1]:
        if len(i)%2:
            print("YES ODD")
        else:
            print("YES EVEN")
    else:
        print("NO")