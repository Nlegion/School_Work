a=int(input())
s=1000
for i in range(a):
    if i<s:
        s=i
if s<-15:
    print("YES")
else:
    print("NO")

