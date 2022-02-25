# Гусь стоит 25 пиастров, утка – 10, а курица 7. Всего нужно купить n птиц, а в наличии есть m пиастров. Сколько каких птиц можно купить на эти деньги?
#
# Формат ввода
# Вводится два числа –n и m.

from itertools import product

n = int(input())
m = int(input())

res = []
for g, u in product(range(n), repeat=2):
    k = n - (g + u)
    if k >= 0 and g + u + k == n and g * 25 + u * 10 + k * 7 == m:
        res.append((g, u, k))
print('\n'.join([' '.join(map(str, row)) for row in res]))
