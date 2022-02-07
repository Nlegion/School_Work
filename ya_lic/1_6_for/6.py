# Напишите программу, которая для введенного числа находит сумму его делителей,
# включая единицу и само число.

numb = int(input())
z = 0
if numb != 1:
    for i in range(numb - 1, 1, -1):
        if (numb % i == 0):
            z += i
    print(numb + z + 1)
else:
    print(1)
