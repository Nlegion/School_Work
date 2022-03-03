a, b = int(input()), int(input())
while a != b:
    if (a // 2 >= b) and (a % 2 == 0):
        print('Разделить на 2')
        a //= 2
    else:
        print('Вычесть 1')
        a -= 1
