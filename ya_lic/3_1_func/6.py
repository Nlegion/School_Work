# Для построения графика функции нужно записать пары значений (x, y) в таблицу. Напишите функцию graph(func), которая принимает в качестве аргумента строку с записанной в ней зависимостью y от x и выводит таблицу значений в диапазоне по x от -10 до 10 (разделитель – символ табуляции).
#
# Для вычисления значений воспользуйтесь встроенной функцией eval(expression). В качестве аргумента ей передается строка, представляющая собой код на python, возвращается результат его выполнения.
#
# Пример
# Ввод	Вывод
# graph('2 * x - 5')
# x	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1	0	1	2	3	4	5	6	7	8	9	10
# y	-25	-23	-21	-19	-17	-15	-13	-11	-9	-7	-5	-3	-1	1	3	5	7	9	11	13	15
# История решений

def graph(f):
    print('x' + '\t' + '\t'.join([str(_) for _ in range(-10, 11)]))
    print('y' + '\t' + '\t'.join([str(eval(f)) for x in range(-10, 11)]))