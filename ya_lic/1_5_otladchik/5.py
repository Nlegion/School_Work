# Координатная плоскость разделена на 2 части прямой
# y = k x + b
# Напишите программу, которая посчитает, сколько из введённых точек попало в полуплоскость выше прямой, ниже прямой, а сколько на прямую.
#
# Формат ввода
# В первых двух строках вводятся целые коэффициенты прямой k и b.
# Затем вводятся пары целых чисел – координата х и координата у точки, пока не будет введена строка END.
#
# Формат вывода
# Вывести количество точек, попавших в каждую полуплоскость и на прямую в формате:
# Выше прямой: {количество}
# Ниже прямой: {количество}
# На прямой: {количество}
# Если в какую-то группу не попало ни одной точки, то выводить отчёт для неё не нужно.
# Хотя бы одна точка точно будет введена.

k = int(input())
b = int(input())
x1 = 0
y1 = 0
x2 = 0
y2 = 0
ko = 0
kl = 0
ku = 0
x = input()
while x != 'END':
    x = int(x)
    y = int(input())
    d = y - b - k * x
    if d < 0:
        ku += 1
    elif d > 0:
        ko += 1
    else:
        kl += 1
    x = input()
if ko:
    print('Выше прямой:', ko)
if ku:
    print('Ниже прямой:', ku)
if kl:
    print('На прямой:', kl)