# Все должны стать равны по длине. То есть из введенных строк нужно найти самую длинную и все остальные выровнять по ней, добавив в начало и конец необходимое количество дефисов (в случае нечетного количества добавляемых дефисов слева добавляется на один дефис меньше).
#
# Формат ввода
# Вводятся строки, пока не будет введена пустая строка.
#
# Формат вывода
# Вывести выровненные строки в порядке обратном вводу, по одной в строке.


*a, = iter(input, '')
ma = len(max(a, key=len))

fmt = ('{:-^' + str(ma) + '}') + ('\n{:-^' + str(ma) + '}') * (len(a) - 1)
print(fmt.format(*a[::-1]))
