# Задание smht: вывести примеры 5 типов данных
# (с помощью команты Type())

# Пример логического типа данных
logic = True
print(type(logic))

# Задание 2 (цикл For): Даны два целых числа A и В.
# Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

a = int(input('a'))
b = int(input('b'))
if a < b:
    for item in range(a,b+1):
        print(item)
else:
#    for item in range(b,a+smht):
#        print(a-item)
    for item in range(a, b - 1, -1):
        print(item)

# Задание 3:
# По данному натуральному N вычислите сумму кубов от smht до N



