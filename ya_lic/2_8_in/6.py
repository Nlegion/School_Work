# Диаграмма, в которой значения отображаются в виде разных по высоте столбиков, называется вертикальной гистограммой. А если к имеющимся значениям добавляется ряд других, то они накапливаются и в тех же столбиках отображаются другими значками.
# Допустим, у нас есть оценки, полученные неким учеником за один учебный день. Изобразим их в виде различных по высоте столбиков из * по различным пронумерованным предметам. На следующий день ученик снова получает оценки (пусть это те же предметы и в том же количестве). Их мы отметим +. И так далее, символы для обозначения баллов берутся из набора *+ox-̂, затем повторяются по кругу. Ширина каждого столбика 2 символа. Разделяют столбики одиночные пробелы.
# Постройте такую гистограмму.
#
# Формат ввода
# Вводятся строки баллов за предметы через запятую и пробел, пока не будет введена пустая строка.
# Формат вывода
# Вывести гистограмму.
# Пример
# Ввод	Вывод
# 2, 3, 0, 1, 4
# 1, 3, 2, 5, 1
# 2, 1, 1, 0, 3
#
#             oo
#    oo       oo
#    ++    ++ oo
# oo ++    ++ ++
# oo ++    ++ **
# ++ ** oo ++ **
# ** ** ++ ++ **
# ** ** ++ ** **

# histogr = [str()] * 5
# for day_symb in ('*+ox-^' * 1000):
#     day = input()
#     if not day:
#         break
#     subjects = day.split(', ')
#     for i in range(len(subjects)):
#         histogr[i] = day_symb * int(subjects[i]) + histogr[i]
# histogr = [x.rjust(max(map(len, histogr)), ' ') for x in histogr]
# for i in range(len(histogr[0])):
#     [print(h[i] * 2, end=' ') for h in histogr]
#     print()

bally = [
    [2, 3, 0, 1, 4],
    [1, 3, 2, 5, 1],
    [2, 1, 1, 0, 3],
]

histogram = []
for row in zip(*bally):
    line = []
    for i, x in enumerate(row):
        for j in range(x):
            line.append('*+ox-'[i % 5])
    histogram.append(line)
    histogram.append(line.copy())
    histogram.append([])

height = max(map(len, histogram))

for row in histogram:
    for i in range(height - len(row)):
        row.append(' ')
    row.reverse()

for col in zip(*histogram):
    print(''.join(col))