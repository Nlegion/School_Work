# Запросите у пользователя ввод 10 чисел.
# цикл While обязателен
l = []
item = 1
while item <= 10:
    l.append(int(input('Введите целое число')))
    item += 1
print(l)
