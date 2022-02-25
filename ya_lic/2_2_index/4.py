# Вводится номер буквы английского алфавита (используется только верхний регистр). Вывести эту букву и следующие три за ней. Если алфавит закончился, продолжить его циклически с начала.
#
# Английский алфавит: ABCDEFGHIJKLMNOPQRSTUVWXYZ

ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
index = n - 1
for _ in range(3 + 1):
    print(ab[index % len(ab)], end='')
    index += 1
