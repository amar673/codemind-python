a=int(input())
b=str(a)
c=set(b)
if len(c)==len(b):
    print("Unique Number")
else:
    print("Not Unique Number")