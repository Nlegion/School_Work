# Строки могут быть разными, с числами и без. Среди множества вводимых строк нужно выбрать те, в которых больше всего чисел, а среди отобранных ту, в которой их сумма минимальна.
#
# Напишите такую программу.
#
# Формат ввода
# Вводятся строки.
#
# Формат вывода
# Нужно вывести наименьшую из сумм чисел для строк, в которых больше всего чисел. Если строк с числами нет, то вывести -1.
#
# Пример 1
# Ввод	Вывод
# Расстояние до Луны в среднем 384000 км.
# До Плутона со скоростью 8000 км/с лететь около 750000 с.
# Марсианские сутки длятся 24 часа 37 минут.
# Земная ось наклонена под углом 23 градуса.

import re

s = input().strip()

lst = [list(map(int, re.findall(r'\d+', i))) for i in s.split('\n')]
print(min(map(sum, filter(lambda x: len(x) == len(max(lst, key=len)), lst))) if re.search(r'\d', s) else -1)
