for i in range(int(input())):
    s=input()
    for j in s:
        if j.isdigit():
            print("Yes")
            break
    else:
        print("No")
