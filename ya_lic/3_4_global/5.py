# Представьте, что вам нужно много раз находить количество делителей числа. Но эти числа могут повторяться. Чтобы не делать одну и ту же работу несколько раз, вы записали во внешнюю переменную divisors словарь: ключ – число, значение – количество делителей, и просто проверяете, есть ли такое число в словаре.
# Напишите функцию number_of_divisors(n) для поиска количества делителей числа n.
#
# Пример
# Ввод	Вывод
# print(number_of_divisors(2000000000))
# print(number_of_divisors(6))
# print(number_of_divisors(6))
# print(number_of_divisors(2000000000))
# print(divisors)
# 110
# 4
# 4
# 110
# {2000000000: 110, 6: 4}
# Примечания
# В задаче нельзя использовать инструкцию global.

def number_of_divisors(N):
    c = []
    count = 0
    for j in range(1, int(N ** 0.5) + 1):
        if N % j == 0:
            count += 1
    if float(N ** 0.5) != int(i ** 0.5):
        c.append(2 * count)
    else:
        c.append(2 * count - 1)
    return count
