import math
n=int(input())
c=int(math.sqrt(n))
j=c*c
if j==n:
    print(True)
else:
    print(False)