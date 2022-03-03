s = []
for item in range(3):
    s.append(len(input()))
s.sort()
for itr in range(s[2], s[1], -s[0]):
    print(itr, '', end='')
