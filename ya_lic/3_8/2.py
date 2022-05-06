# Среди большого количества целых чисел нужно найти такое, у которого сумма цифр минимальна. Если таких несколько, то выбираем с наибольшей длиной. Если и тут есть варианты, то выбрать наименьшее по значению.
#
# Постарайтесь решить задачу в одну строку.
#
# Формат ввода
# Вводятся целые числа по одному в строке.
#
# Формат вывода
# Вывести число с наименьшей суммой цифр, при равенстве сумм с наибольшей длиной, при равенстве длин с наименьшим числовым значением.
#
# Пример 1
# Ввод	Вывод
# 20010
# 1000002
# 2000001
# 1002
# 12
# 21
# 201
# 102
# 1000002

import sys

print(min(list(map(int, sys.stdin)), key=lambda x: (sum(map(int, str(x))), -len(str(x)))))