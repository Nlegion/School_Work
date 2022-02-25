# Разложите составное число на его простые сомножители. Результат запишите в виде примера:
# 48 = 2 * 2 * 2 * 2 * 3

n = int(input())
print(n, '= ', end='')
i = 2
res = []
while i * i <= n:
    if n % i == 0:
        n //= i
        res.append(i)
    else:
        i += 1
res.append(n)
print(*res, sep=' * ')
