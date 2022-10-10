a,b=map(str,input().split())
c=0
for i in a:
    if i in b and b.count(i)>=a.count(i):
            c+=1
if c>=len(a):
    print(True)
else:
    print(False)