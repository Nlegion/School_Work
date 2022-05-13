# Ждать и догонять всегда не очень приятно. Напишите функцию days_left(), которая определит, сколько осталось дней от сегодняшнего дня до переданной даты.
#
# Дата в функцию передается в виде строки из трех чисел, разделенных точками, – дня, месяца и года.
#
# Пример 1
# Ввод	Вывод
# print(days_left('31.12.2022'))
# 364
# Пример 2
# Ввод	Вывод
# print(days_left('28.01.2022'))
# 27

from datetime import datetime


def days_left(date):
    today = datetime.today()
    date = datetime.strptime(date, '%d.%m.%Y')
    return (date - today).days