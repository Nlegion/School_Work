a = int(input('введите число А'))
b = int(input('введите число B'))
if a == 0:
    if b == 0:
        print('x - любое число')
    else:
        print('Решений нет')
else:
    x = -b / a
    print('Одно решение: x=', x)
