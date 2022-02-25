# Вводятся слова. Выведите только те из них, в которых нет повторяющихся букв. Ввод заканчивается пустой строкой.
s = 1
list = []
while s != '':
    s = input()
    i = 0
    s1 = [item for item in s]
    for item in s1:
        if s1.count(item) > 1:
            i += 1
    if i == 0:
        list.append(s)
for itr in list:
    print(itr)
