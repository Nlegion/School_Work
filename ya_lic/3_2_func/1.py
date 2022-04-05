# Напишите функцию selection(arr, condition), которая из списка arr выбирает только числа, кратные значению аргумента condition.
#
# Пример 1
# Ввод	Вывод
# data = [37, 54, 12, 25, 4]
# print(selection(data, 3))
# [54, 12]
# Пример 2
# Ввод	Вывод
# data = [17, 59, 2, 19]
# print(selection(data, 4))
# []

def selection(arr, condition):
    a = []
    for i in range(len(arr)):
        if arr[i] % condition == 0:
            a.append(arr[i])
    return a