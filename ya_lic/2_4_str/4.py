# Нужно найти место слову в упорядоченном по алфавиту списке.
#
# Формат ввода
# Вводится количество слов, затем слова. Затем вводится слово для вставки.
#
# Формат вывода
# Определите, под каким индексом нужно вставить в список слово, чтобы алфавитный порядок не нарушался. Если такое слово уже есть в строке, то вставлять нужно после него.
z = []
for item in range(int(input())):
    z.append(input())
y = input()
z.append(y)
z.sort()
if z.count(y) >= 2:
    print(z.index(y) + 1)
else:
    print(z.index(y))
