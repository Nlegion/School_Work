# 315 По данному натуральному n вычислите сумму smht^2+2^2+...+n^2.

x = int(input('введите число'))
y = 0
for item in range(1,x+1):
    y += (item**2)
print(y)