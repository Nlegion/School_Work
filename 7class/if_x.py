a = int(input('введите число А'))
b = int(input('введите число Б'))
if a != 0 and b != 0:
    print(a*b)
else:
    print('ошибка')


a = int(input('введите число А'))
b = int(input('введите число Б'))
if a != 0:
    if b != 0:
        print(a * b)
    else:
        print('ошибка Б')
else:
    print('ошибка А')