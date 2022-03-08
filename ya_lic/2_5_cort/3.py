z = ''
n = 0
lst = []
while z != 'разбитое корыто':
    z = input()
    if z != 'разбитое корыто':
        lst.append(z)
        n += 1
a = lst

for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(a[j]) > len(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]
        elif len(a[j]) == len(a[j + 1]):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
for word in a:
    print(word)
