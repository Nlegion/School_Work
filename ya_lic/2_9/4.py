# В строке через пробел записано некоторое количество целых десятичных чисел.
#
# Напишите программу, которая составит список словарей, в которых каждое число будет характеризоваться количеством разрядов, нулей и единиц в двоичном представлении. Формат вывода смотрите в примерах.
#
# Формат ввода
# Строка из целых чисел, разделённых пробелами.
#
# Формат вывода
# Вывести список словарей, в котором для каждого из чисел записаны его характеристики по ключам:
#
# digits – количество разрядов в двоичном представлении числа;
# units – количество единиц в двоичном представлении числа;
# zeros – количество нулей там же.
# Пример
# Ввод	Вывод
# 5 8 12
# [{'digits': 3, 'units': 2, 'zeros': 1}, {'digits': 4, 'units': 1, 'zeros': 3}, {'digits': 4, 'units': 2, 'zeros': 2}]

def task(arr):
    r = []
    for a in arr:
        if a == 0:
            d = {'digits': 1, 'units': 0, 'zeros': 1}
            r.append(d)
        else:
            u, z = 0, 0
            while (a > 0):
                if a % 2 == 0:
                    z += 1
                else:
                    u += 1
                a = a // 2
            d = {'digits': u + z, 'units': u, 'zeros': z}
            r.append(d)
    return r


arr = list(map(int, input().split(' ')))
print(task(arr))