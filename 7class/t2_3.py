# вывести нечетные элементы массива
a = [1, 2, 3, 4, 5]
for item in range(len(a)):
    if (item % 2) == 0:
        print(a[item])