# В палитре огромное количество цветов, например, в модели RGB их 16777216. Напишите программу, которая считает количество повторяющихся цветов.
#
# Формат ввода
# Вводится количество наборов, затем для каждого набора вводится количество цветов в наборе и сами цвета в виде строки в 16-ричном представлении.
sets = int(input())
list = []
unic = set()
ununic = 0
for item in range(sets):
    count = int(input())
    for itr in range(count):
        list.append(input())
for it in list:

    if list.count(it) != 1:
        unic.add(it)
        ununic += 1
print(len(unic), ununic)
