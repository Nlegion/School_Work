# Если смотреть вдаль, то видеть мы будем хотя бы частично только дома, которые выше стоящих ближе. Напишите программу, выводящую высоты зданий, которые видны из данной точки в порядке их расположения. Выводить через ».
#
# Формат ввода
# Вводится строка из натуральных чисел через пробел.
# Формат вывода
# Выведите в одну строку через » только высоты тех зданий, которые видны из данной точки.
# Пример 1
# Ввод	Вывод
# 8 2 12 12 3 15
# 8>>12>>15
# Пример 2
# Ввод	Вывод
# 5 3 2 2 1
# 5
s = input().split()
a = []
maxS = int(s[0])
a.append(s[0])
for i in range(len(s) - 1):
    if int(s[i]) < int(s[i + 1]):
        if maxS < int(s[i + 1]):
            a.append(s[i + 1])
            maxS = int(s[i + 1])
print('>>'.join(a))
