# Запросите у пользователя числа, пока не будет введен 0.
# цикл While обязателен
l = []
z = 1
item = 1
while z != 0:
    z = int(input('Введите целое число'))
    l.append(z)
    item += 1
print(l)
