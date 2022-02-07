# Быть первым в чем-то здорово и почетно. Но вторые тоже заслуживают внимания.
# Найдите среди введенных чисел второй максимум, то есть число, которое было бы максимальным, если бы первого максимума не было.
# Формат ввода
# Вводятся числа (не менее трех), пока не будет введено число, которое по модулю не меньше 1000.
# Формат вывода
# Вывести второй максимум.

x = -100
first_max = -100
second_max = -100
while abs(x) < 1000:
    x = int(input())
    if x < 1000:
        if x > first_max:
            second_max, first_max = first_max, x
        elif x > second_max:
            second_max = x
print(second_max)