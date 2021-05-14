a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in a: #перечисление всех элементов списка
    print(item)

for item in range(len(a)): #обращение к элементам списка по индексу
    print(a[item])

#задание 1: Выведите все элементы списка с четными индексами
for item in range(0,len(a),2):
    print(a[item])

#задание 2: Выведите все четные элементы списка.
for item in a:
    if item % 2 == 0:
        print(item)