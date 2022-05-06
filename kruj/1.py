# 1
x = int(input("введите количество секунд"))
h = x // 3600
m = (x - h * 3600) // 60
s = x - (h * 3600 + m * 60)
print(h, m, s)

# 2
z = int(input())
print(z * 1 + z * 11 + z * 111)
