# Напишите функцию total() для подсчета общей калорийности заказанных блюд. В качестве аргумента в функцию передается список строк: блюдо и его калорийность через пробел. После каждого вызова калорийность суммируется и выводится общий итог в виде (блюда отсортированы в алфавитном порядке):
#
# <Блюдо> - <количество порций> - <калорийность всех порций, точность до десятых> kCal
# ...
# ------
# Total: <общая калорийность с точностью до 1 знака после запятой> kCal
# В конце – пустая строка для разделения вызовов функции.
#
# Пример
# Ввод	Вывод
# data = ["Ice cream, strawberry 192",
#         "Puff pastry with protein cream 461"]
# total(data)
# data = ["Orange juice drink 54.5",
#         "Ice cream, strawberry 192",
#         "Puff pastry with protein cream 461"]
# total(data)
# Ice cream, strawberry - 1 - 192.0 kCal
# Puff pastry with protein cream - 1 - 461.0 kCal
# ------
# Total: 653.0 kCal
#
# Ice cream, strawberry - 2 - 384.0 kCal
# Orange juice drink - 1 - 54.5 kCal
# Puff pastry with protein cream - 2 - 922.0 kCal
# ------
# Total: 1360.5 kCal

e = {}
a = []


def total(sp):
    global e
    global a
    for i in range(len(sp)):
        s = ''
    for j in range(len(sp[i]) - 1, 0, -1):
        if sp[i][j] == ' ' and sp[i] not in e:
            e[sp[i][:len(sp[i]) - len(s) - 1]] = [float(s[::-1]), 0]
            a.append(sp[i][:len(sp[i]) - len(s) - 1])
            break
    else:
        s += sp[i][j]
        for i in range(len(a)):
            if a[i] in e.keys():
                e[a[i]][1] = a.count(a[i])
        tot = 0
        sorted_tuple = sorted(e.items())
        e = dict(sorted_tuple)
    for key, value in e.items():
        print(f'{key} - {value[1]} - {(value[0] * a.count(key)):.1f} kCal')
        tot += value[0] * a.count(key)
    print('------')
    print(f'Total: {tot:.1f} kCal')
    print()
