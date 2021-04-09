import sys

line = sys.stdin
lineout = sys.stdout
z = 0
test = ''
for item in line:
    z += 1
    test = test + item
    if (z >= 80) & (item == ' '):
        z = 0
        test = test + '\n'
for item in test:
    lineout.write(item)
