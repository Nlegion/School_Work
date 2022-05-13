# Напишите функцию circuit_resistance() для расчета сопротивления цепи. Функция вызывается с аргументами:
#
# произвольное количество значений сопротивления (целые числа);
# connection – тип соединения (serial, parallel) – именованный аргумент, по умолчанию serial (последовательное);
# conductivity – именованный аргумент, что найти – сопротивление или проводимость, по умолчанию False, то есть определяется сопротивление.
# Функция возвращает вычисленное значение в виде вещественного числа, округлённого до 4 знаков после запятой.
#
# Пример 1
# Ввод	Вывод
# data = [10, 20, 30]
# print(circuit_resistance(*data))
# 60

#
# def circuit_resistance(*data):
#     t = lambda *data, connection='serial', conductivity=False: (
#         lambda result: 1 / result if conductivity else result)(
#         sum(data) if connection == 'serial' else 1 / sum(1 / r for r in data))
#     return t
def circuit_resistance(*data):
    return lambda *data, connection='serial', conductivity=False: (
        lambda result: 1 / result if conductivity else result)(
        sum(data) if connection == 'serial' else 1 / sum(1 / r for r in data))