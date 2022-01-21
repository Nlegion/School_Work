a = int(input('введите число'))
b = int(input('введите число'))
c = int(input('введите число'))
d = 0
if a > b:
    if a > c:
        d = a
    else:
        d = c
else:
    if b > c:
        d = b
    else:
        d = c
print(d)
