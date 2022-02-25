# Напишите программу, которая выводит все цифры, которых не было во введенном числе. Выводить в одну строку через пробел, порядок не важен.
numbers = [item for item in range(10)]
z = [int(item) for item in input()]
for item in numbers:
    if item not in z:
        print(item, ' ', end='')
