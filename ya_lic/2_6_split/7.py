# Вводится очень длинное число. Выведите процесс его укорачивания справа и слева по одной цифре за раз, каждый результат с новой строки.
#
# Пример 1
# Ввод	Вывод
# 123456789
# 123456789
# 2345678
# 34567
# 456
# 5

a = input()
p = [a[k:-k] for k in range(1, (len(a) + 1) // 2)]
print(a)
for i in range(len(p)):
    print(p[i])