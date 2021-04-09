inf = open('file2.txt','r',encoding="utf-8")
s1 = inf.readline()
s2 = inf.readline()
inf.close()

with open('file2.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

print(s1,s2)