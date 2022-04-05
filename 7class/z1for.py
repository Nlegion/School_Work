x = 10
y = 0
for item in range(x, y, -2):
    print(item)

x = 10
y = 0
z = 0
for item in range(x):
    y += 1
    z += item
print(z / y)

x = 10
y = 0
z = 0
for item in range(x):
    y += 1
    z += item
print(z ** (1. / y))

x = 0.1
y = '1'
print(int(y) + x)
