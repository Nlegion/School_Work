# Чтобы смоделировать возможные варианты развития событий, упростим ситуацию. Вселенная нашей задачи будет расширяться бесконечно, если сумма масс всех тел, умноженная на произведение констант превышает Очень Важное Число (Very Important Number). Если это значение меньше ОВЧ (VIN), то вселенная расширяется с замедлением и где-то впереди нас ждет Большое Сжатие.
#
# Напишите функцию future(), предсказывающую будущее вселенной.
#
# В глобальной переменной VIN находится значение Очень Важного Числа.
# Функция принимает произвольное количество масс космических тел и произвольное число именованных аргументов – различных фундаментальных констант.
# Если вселенная будет расширяться с ускорением, нужно вернуть строку ACCELERATION, если с замедлением, то DECELERATION, иначе UNCHANGED.
#
# Пример 1
# Ввод	Вывод
# VIN = 3
# mass = [1, 2, 3, 4]
# const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
# print(future(*mass, **const))

from functools import reduce


def future(*mass, **const):
    global VIN
    sum_of_masses = sum(mass) * reduce(lambda x, y: x * y, const.values())
    if sum_of_masses > VIN:
        return 'ACCELERATION'
    elif sum_of_masses < VIN:
        return 'DECELERATION'
    return 'UNCHANGED'