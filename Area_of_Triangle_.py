a,b,c=map(int,input().split())
s=(a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c))**0.5
ar=format(area,".2f")
print(ar)