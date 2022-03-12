# Старик уже много лет ловит рыбу и заметил, что рыбалка будет удачной, если из названий выловленных рыб, не учитывая повторений, можно построить возрастающую последовательность по алфавиту и по длине, и они совпадут.
#
# Проверьте, выполняется ли это условие в данной рыбалке.
#
# Формат ввода
# Вводятся названия рыб, пока не будет введена пустая строка.
#
# Формат вывода
# Если при сортировке названий по длине и по алфавиту получается одна и та же последовательность, выведите YES, если не получается, выведите название первой рыбы (сначала по алфавиту, затем по длине), нарушающей этот порядок.

fish = []
z = 'w'
while z != '':
    z = input()
    fish.append(z)

fish_al = fish[:]
fish_le = fish[:]
for i in range(len(fish_al) - 1):
    for j in range(len(fish_al) - i - 1) :
        if fish_al[j] > fish_al[j + 1]:
            fish_al[j], fish_al[j + 1] = fish_al[j + 1], fish_al[j]
for i in range(len(fish_le) - 1):
    for j in range(len(fish_le) - i - 1):
        if len(fish_le[j]) > len(fish_le[j + 1]):
            fish_le[j], fish_le[j + 1] = fish_le[j + 1], fish_le[j]
out = 'YES'
for al, le in zip(fish_al, fish_le):
    if al != le:
        out = al + ' ' + le
        break
print(out)
