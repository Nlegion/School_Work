# Для сборки очередной модели вечного двигателя вам понадобилось сделать механизм из шестеренок с передаточным числом
# n
# ∕
# m
# . На складе на стеллажах стоят коробки с шестерёнками, только их забыли подписать. Найдите две подходящие шестерёнки или выведите сообщение, что их нет.
# Для решения задачи напишите функцию gears(), которая принимает три аргумента: список списков имеющихся шестерёнок, n и m.
# Возвращает функция кортеж из двух размеров шестерней или (None, None), если они не нашлись. Если подходящих шестерёнок несколько, вернуть любую пару.
# PIC
#
# Пример
# Ввод	Вывод
# data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
# print(gears(data, 30, 7))
# (60, 14)

def gears(rack: list, n: int, m: int):
    a = {}
    b = {}
    for box in rack:
        for gear in box:
            if gear > 0:
                if gear % n == 0:
                    rn = gear // n
                    if rn not in a:
                        if rn in b:
                            return (gear, b[rn])
                        a[rn] = gear
                if gear % m == 0:
                    rm = gear // m
                    if rm not in b:
                        if rm in a:
                            return (a[rm], gear)
                        b[rm] = gear
    return (None, None)