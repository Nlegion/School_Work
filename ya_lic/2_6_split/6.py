# Свобода лучше, чем несвобода. Нам всё введут, а мы выберем.
#
# Напишите программу, которая из одной строки считает:
# строка (разделитель) число (необходимое количество уникальных символов) строка (для анализа)
#
# Затем по первой строке разделить последнюю и выбрать из полученного списка только те слова, в которых уникальных символов не меньше указанного числа.
#
# Формат ввода
# Вводится разделитель, потом число n, потом строка слов, записанных через этот разделитель.
#
# Формат вывода
# Вывести слова, имеющие не меньшее n количество уникальных символов, записанные через этот же разделитель, записанный в обратном порядке.
#
# Пример
# Ввод	Вывод
# -$ 4 Python-$is-$the-$best-$programming-$language-$in-$the-$world
# Python$-best$-programming$-language$-world
# Примечания
# Используйте множественное присваивание и списочное выражение.
#

def cor(w, n):
    m = set(w)
    if len(m) >= n:
        return w


a, n, b = input().split()
n = int(n)
print(*[w for w in b.split(a) if cor(w, n)], sep=a[::-1])
