a = [-3, 2, 2, -2, -3, 0, -2, 2, 0, 1, -3, -1, 2, 2, 2, 0, -2, 2, 0, -1, 2, -3, 2, 1, 0, 1, 1, -1, 2, -2, -1]
count = 0
summ = 0
for item in a:
    if item > 0:
        count += 1
        summ += item
print(summ / count)
