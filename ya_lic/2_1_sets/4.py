# Музыканты в оркестре часто умеют играть на нескольких инструментах. Найдите тех, кто играет только на каком-то одном.
#
# Формат ввода
# Три раза вводятся фамилии музыкантов, пока не будет введена пустая строка.
#
# Сначала те, кто играют на гобое, затем на флейте, потом на саксофоне.
#
# Формат вывода
# Выведите фамилии тех, кто играет только на каком-то одном инструменте.

i = 1
z = []
y = []
for item in range(3):
    while i != '':
        i = input()
        z.append(i)
    if i == '':
        i = 1
    for item_2 in set(z):
        y.append(item_2)
    z = []

for item_3 in y:
    if y.count(item_3) == 1:
        print(item_3)
