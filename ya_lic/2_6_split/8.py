# Гирлянды очень украшают помещение к празднику. Создают ощущение леса, свисающих лиан, тропиков…
#
# Напишите программу, которая из введенного предложения сделает гирлянду: каждое слово будет выводить вертикально вниз по букве, между словами, а также в начале и в конце – нижнее подчеркивание – веревочка, за которую гирлянду можно подвесить куда-нибудь повыше.
#
# И еще после пустой строки нужно вывести антигирлянду – ее отражение в натертом до блеска полу.
#
# Формат ввода
# Вводится строки слов, разделенных пробелами.
#
# Формат вывода
# Вывести каждое слово строки вертикально сверху вниз, в первой строке слова разделены символом подчеркивания и по одному подчеркиванию в начале и в конце.
# Затем вывести пустую строку.
# Затем снова вывести слова вертикально, но так, чтобы начинались слова на нижней строке и снова разделенные символом подчеркивания.
# Во всех остальных случаях для разделения используется пробел.

s = input().split()
print('_' + '_'.join(i[0] for i in s) + '_')
for i in range(1, len(max(s, key=len))):
    print(' ' + ' '.join(w[i] if len(w) > i else ' ' for w in s))
print()
for i in range(len(max(s, key=len)) - 1, 0, -1):
    print(' ' + ' '.join(w[i] if len(w) > i else ' ' for w in s))
print('_' + '_'.join(i[0] for i in s) + '_')
