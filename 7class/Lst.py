ls = [1,12,34,45,76,87,14,99]

print(ls)
for i in range(len(ls)-1):
    for j in range(len(ls)-i-1):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]

print(ls)