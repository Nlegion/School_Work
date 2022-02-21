i = 1
z = 0
while i != 0:
    i = int(input())
    if (100 < i < 999) and (i % 4 == 0):
        z += 1
print(z)