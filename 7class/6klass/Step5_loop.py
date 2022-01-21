x = int(input('введите число'))

print('for')
for item in range(x):
    print(item)

print('while')
item_2 = 0
while item_2 <= x:
    item_2 += 1
    print(item_2)