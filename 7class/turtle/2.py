#Известно, что X кг шоколадных конфет стоит A рублей,
# а Y кг ирисок стоит B рублей.
# # Определить, сколько стоит 1 кг шоколадных конфет,
# 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.
# Построить диалог для ввода данных и вывода результата.

x = int(input('Введите кг шоколадных конфет'))
a = int(input('Введите стоимость шоколадных конфет'))
y = int(input('Введите кг ирисок'))
b = int(input('Введите стоимость ирисок'))

print('1 кг шоколадных конфет стоит:',x/a)
print('1 кг ирисок стоит:',y/b)
print((x/a)/(y/b))