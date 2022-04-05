a=int(input())
k=0
while a!=0:
    if a//1000==0 and a%4==0:
        k+=1
    a=int(input())
print(k)