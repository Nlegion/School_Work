# Сложные проценты, в отличие от простых, начисляются по истечении каждого периода на сумму, включающую проценты от предыдущего периода. Однако, если вы решите забрать свои деньги до истечения договорного периода, то процент уменьшается до одного и прибыль рассчитывается только пропорционально той доле периода, которая прошла.
#
# Напишите программу для расчёта полученной прибыли.
#
# Формат ввода
# Вводится целое число – сумма вклада.
# Затем вещественное число – процент прибыли за год.
# Затем число – через какое количество лет вы решили забрать свой вклад.
#
# Формат вывода
# Если прошло целое количество лет, то за каждый начисляется указанный процент, который прибавляется к сумме вклада, а следующие проценты считаются с новой суммы. Если же количество лет не целое, то за нецелую часть года проценты начисляются пропорционально прошедшей части и в размере 1%.
#
# Выведите конечную сумму.

n = int(input())
p = float(input())
t = float(input())
for i in range(int(t // 1)):
    n += (n / 100) * p
if t == t // 1:
    print(n)
    exit()
x = t - (t // 1)
n += n * x * 0.01
print(n)