# В каждой строке нужно вывести номер строки, повторенный количество раз, равное номеру этой строки.
# Вводится цифра 1 < n < 9. Выведите n строк с повторениями цифр.

n = int(input())
for item in range(1, n + 1):
    for item_2 in range(1, item + 1):
        print(item, end='')
    print('')
