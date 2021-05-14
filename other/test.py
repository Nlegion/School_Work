x = float(input('введите число'))
if x < -150:
    print(5 * (x ** 2) + 1)
elif -150 < x < 0:
    print(4 * abs(x))
else:
    print(5 * (x ** 2) - 7 * x)
