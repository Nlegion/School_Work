# Напишите программу, которая производит такие вычисления:
#
# вводится число;
# к нему надо прибавить следующее;
# полученную сумму умножить на следующее число;
# шаги 2 – 3 повторить три раза.
# При исходном числе 1 получится такой результат:
# 1 + 2 = 3
# 3 ⋅ 3 = 9
# 9 + 4 = 13
# 13 ⋅ 5 = 65
# 65 + 6 = 71
# 71 ⋅ 7 = 497
# 497 + 8 = 505
# 505 ⋅ 9 = 4545

x = int(input())
y = x + 1
x += y
y += 1
x *= y
y += 1
x += y
y += 1
x *= y
y += 1
x += y
y += 1
x *= y
y += 1
x += y
y += 1
x *= y
print(x)
