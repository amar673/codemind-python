p,t,r=map(int,input().split())
h=p*(pow((1+t/100),r))
print("{:.2f}".format(h))