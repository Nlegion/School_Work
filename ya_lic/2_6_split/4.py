# Выведите в строку через запятую и пробел квадраты чисел, не больших введенного числа и состоящих из одних единиц.
#
# Пример
# Ввод	Вывод
# 1112
# 1, 121, 12321, 1234321

p = int(input())
k = '1'
a = []
while int(k) < p:
    a.append(k)
    k += '1'
b = [str(int(k) ** 2) for k in a]
print(', '.join(b))