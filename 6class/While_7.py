#smht. По данному целому числу N распечатайте все квадраты
# натуральных чисел, не превосходящие N, в порядке возрастания.

#2. Дано целое число, не меньшее 2.
#Выведите его наименьший натуральный делитель, отличный от smht.

n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1

i = 2
while n % i != 0:
    i += 1
print('наименьший натуральный делитель=',i)


