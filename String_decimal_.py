for i in range(int(input())):
    a=input()
    c=0
    for j in range(len(a)):
        if a.isdigit()==0:
            c=1
            break
    if c==1:
        print(False)
    else:
        print(True)