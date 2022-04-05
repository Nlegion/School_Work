# Говорят, молния чаще всего ударяет в самые высокие предметы, а если они одинаковой высоты, то в те, в которых больше железа.
#
# Отсортируйте возможные места удара молнии в порядке уменьшения вероятности удара.
#
# Формат ввода
# Вводится количество мест, затем для каждого места вводится сначала высота над окружающим пейзажем (целое число), затем относительное содержание железа (вещественное число).
#
# Формат вывода
# Выведите кортежи (высота, содержание железа) в порядке убывания сначала высоты, а при одинаковой высоте в порядке убывания содержания железа).
#
# В задаче нельзя пользоваться стандартной сортировкой.

n = int(input())
h = [0] * n
p = [0.0] * n
for i in range(n):
    h[i] = int(input())
    p[i] = float(input())
for i in range(n - 1):
    for j in range(i + 1, n):
        if h[j] > h[i] or (h[j] == h[i] and p[j] > p[i]):
            h[i], h[j] = h[j], h[i]
            p[i], p[j] = p[j], p[i]
for i in range(n):
    print((h[i], p[i]))