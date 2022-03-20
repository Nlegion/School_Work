# Напишите функцию next_prime_number(), которая после каждого вызова выводит следующее простое число. Первое простое число – это 2.
#
# Пример 1
# Ввод	Вывод
# next_prime_number()
# next_prime_number()
# next_prime_number()
# next_prime_number()
# next_prime_number()
# next_prime_number()
# 2
# 3
# 5
# 7
# 11
# 13
# Пример 2
# Ввод	Вывод
# next_prime_number()
# 2
def next_prime_number():
    def isprime(n):
        i = 2
        while i * i <= n and n % i != 0:
            i += 1
        return i * i > n

    global p
    p += 1
    while not isprime(p):
        p += 1
    print(p)


p = 1
