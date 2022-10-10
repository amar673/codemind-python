s=input()
k=""
s=set(s)
for i in s:
    if i.isdigit():
        k+=i
k=sorted(k)
for i in k:
    if int(i)%2==0:
        k.remove(i)
        k=k[::-1]
        k.append(i)
        print("".join(k))
        break
else:
    print(-1)