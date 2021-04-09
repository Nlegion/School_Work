inf = open('file.txt','r')
s1 = inf.readline()
s2 = inf.readline()
inf.close()

with open('file.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

print(s1,s2)