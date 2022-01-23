# Очень секретное место, это Поле чудес! Лиса и Кот согласились отвести туда Буратино только с завязанными глазами. Но ему так хочется запомнить дорогу!
# Напишите программу, которая определит, куда его в конце концов привели относительно начальной точки. В начальной точке Буратино смотрит по направлению оси y, то есть вверх.
#
# Формат ввода
# Вводятся строки, это могут быть слова направо, налево, шаг, а могут и какие-то другие, не связанные с перемещением.
# шаг означает перемещение на единичный отрезок;
# направо или налево – поворот без перемещения.
# На все другие слова можно не обращать внимания. Последнее введенное слово – СТОП.
#
# Формат вывода
# Выведите, где оказался Буратино в конце концов по отношению к исходному положению. Например, если он находится в точке, которая правее на 3 и ниже на 2, то нужно вывести 3 -2.

dim = ((0, 1), (1, 0), (0, -1), (-1, 0))
pos = [0, 0]
cur = 0
while True:
    move = input()
    if move == 'СТОП':
        break
    if move in ('налево', 'направо'):
        cur += [-1, 1][move == 'направо']
        if abs(cur) == 4:
            cur = cur % 4
    if move == 'шаг':
        pos = list(map(sum, zip(pos, dim[cur])))
print(*pos)
