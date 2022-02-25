# Выведите слово так, как будто ему что-то мешает произноситься.
# Каждую букву нужно вывести столько раз, каков ее номер в строке.строке

st = input()
list = [item for item in st]
for item in range(len(list) + 1):
    for iter in range(item):
        print(list[item - 1], end='')
