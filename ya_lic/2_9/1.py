# В палеонтологии принята периодизация геохронологических эпох с различной степенью детализации. Примем в задаче довольно крупное деление на эры, временные рамки (от указанной даты и дальше в прошлое) которых показаны на рисунке.
# Так, например, кайнозой (Cenozoic) будем считать продолжающимся со 145 млн лет назад (не включая) и до настоящего времени, мезозой (Mesozoic) – от 300 (не включая) до 145 млн лет назад и так далее.
# PIC
#
# Формат ввода
# Вводятся строки, в которых записан возраст находок в тысячах лет, пока не будет введена пустая строка.
# Формат вывода
# Выведите, к какому периоду они относятся.
# Пример
# Ввод	Вывод
# 3664034
# 1999114
# 4160094
# 335
# 2406460
# 561618
# 170003
#
# Archaea
# Proterozoic
# Archaea
# Cenozoic
# Proterozoic
# Paleozoic
# Mesozoic

er = {"Archaea": (4500, 2800),
      "Proterozoic": (2800, 635),
      "Paleozoic": (635, 300),
      "Mesozoic": (300, 145),
      "Cenozoic": (145, 0)}
a = input()
while a:
    print(*[eras for eras in er if er[eras][0] > int(a) // 1000 >= er[eras][1]])
    a = input()