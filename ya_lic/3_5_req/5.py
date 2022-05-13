# Вася среди всех чисел с четной длиной старается найти счастливые, но считать сумму левой и правой половин числа, чтобы проверить, счастливое ли оно, ему не хочется. Помогите Васе, напишите рекурсивную функцию happy_number(), которая по введенному числу с четной длиной вернет список из двух сумм – левой и правой половин числа.
#
# Глобальные переменные использовать нельзя, а рекурсию использовать – обязательно!
#
# Пример 1
# Ввод	Вывод
# print(happy_number(12342143))
# [10, 10]
# Пример 2
# Ввод	Вывод
# print(happy_number(96251231254621))
# [28, 21]
def happy_number(c, a=0, b=0):
    c = str(c)
    if len(c) == 0:
        return [a, b]
    a += int(c[0])
    b += int(c[-1])
    c = c[1:-1]
    return happy_number(c, a, b)