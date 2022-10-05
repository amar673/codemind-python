for _ in range(int(input())):
    a=int(input())
    temp=a
    rev=0
    while(a):
        rem=a%10
        rev=(rev*10)+rem
        a=a//10
    if rev==temp:
        print(True)
    else:
        print(False)