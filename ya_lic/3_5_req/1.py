# Алгоритм вычисления функции func(n) для целых неотрицательных чисел определяется следующим образом:
# если n = 0, то func(n) = 0;
# если n > 0 и кратно 3, то func(n) = func(n / 3) + 1;
# если n не кратно 3, то func(n) = 2 + func(n - 1).
#
# Напишите функцию func(n).
#
# Пример 1
# Ввод	Вывод
# print(func(6))
# 5
# Пример 2
# Ввод	Вывод
# print(func(10000))
# 24