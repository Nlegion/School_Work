# Из трех введенных строк найдите буквы, которые встречаются хотя бы в двух из них. Выведите эти буквы без повторений подряд в одной строке в любом порядке.

z = input()
y = input()
x = input()
a = []

for item in z:
    if item in y or item in x:
        if item not in a:
            a.append(item)
for item_2 in y:
    if item_2 in x:
        if item_2 not in a:
            a.append(item_2)
st = ''.join([str(item) for item in a])
print(st)