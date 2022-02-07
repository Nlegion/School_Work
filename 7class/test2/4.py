v = 32000
n = 16
height = 800
width = 600
i = 0
if n % 2 == 0: # определение i
    while 2 ** i < n:
        i += 1
k = 800 * 600
I = k * i
t = I / v
print(t)
