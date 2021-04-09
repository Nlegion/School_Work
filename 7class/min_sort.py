arr = [1,2,41,454,23,65,87,234,567,234,63, 80, 62, 69, 71, 37, 12, 90, 19, 67]

for i in range(len(arr) - 1):
    m = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[m]:
            m = j
        j = j + 1
    arr[i], arr[m] = arr[m], arr[i]
print(arr)