x = 12123
d = map(int, str(x))
y2 = 0
for item_2 in d:
    if item_2 < 4:
        y2 += item_2
print(y2)