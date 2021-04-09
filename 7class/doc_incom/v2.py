import sys

line = sys.stdin.read()
z = 0
for item in line:
    z += 1
    if (z >= 80) & (item == ' '):
        z = 0
        sys.stdout.write(item + '\n')
    else:
        sys.stdout.write(item + '\r')
