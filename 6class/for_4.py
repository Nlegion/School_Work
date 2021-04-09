# Даны два целых числа A и B (при этом A ≤ B).
# Выведите все числа от A до B включительно.
a = int(input('введите число А'))
b = int(input('введите число Б'))
if a <= b:
    for item in range(a, b):
        print(item)
else:
    print("ошибка")
       