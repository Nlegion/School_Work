# Выведите n строк по n чисел от 1 до n2 через символ табуляции.
z = int(input())
num = 0
for item in range(z):
    for item_2 in range(z):
        num += 1
        if num % z != 0:
            print(f'{num}\t', end='')
        else:
            print(num)
