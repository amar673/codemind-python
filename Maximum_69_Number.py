i=int(input())
b=str(i)
h=str()
k=0
for j in range(0,len(b)):
    if k==0 and b[j]!="9":
        h+="9"
        k=1
    else:
        h+=b[j]
print(int(h))
    
    
        
    