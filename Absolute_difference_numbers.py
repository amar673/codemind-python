a,b=map(int,input().split())
c=list(str(a))
e=c[:b]
ei=c[-b:]
e=int("".join(e))
ei=int("".join(ei))
print(abs(e-ei))
