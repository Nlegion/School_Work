# Задание smht.
x = int(input('введите имя'))
print("Привет", x, "!")
# Задание 2.
x = int(input('введите число'))
print("Введено число", x, "следующее число", x + 1)
# Задание 3.
x = int(input('введите число'))
y = int(input('введите число'))
print(x + y, x - y, x / y, x * y)
# Задание 4.
x = int(input('введите количество дней'))
print(x, 'дней это', x * 24, 'часов', x * 24 * 60, 'минут', x * 24 * 60 * 60, 'секунд')
# Задание 5.
x = int(input('введите число'))
y = int(input('введите число'))
if x < y:
    print(x)
else:
    print(y)
# Задание 6.
for item in range(1, 11):
    print(item)
# Задание 7.
while x < 11:
    print(x)
    x += 1
