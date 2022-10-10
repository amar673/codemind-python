s=input()
s=list(s)
k=s.count('L')
m=s.count('U')
m1=s.count('D')
k1=len(s)-k-m-m1
if k==k1 and m==m1 :
    print(True)
else:
    print(False)
