co=0
for _ in range(int(input())):
    c=input()
    if c=='++X' or c=='X++':
        co+=1
    else:
        co-=1
print(co)
