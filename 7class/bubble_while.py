arr = [1,2,41,454,23,65,87,234,567,234,63, 80, 62, 69, 71, 37, 12, 90, 19, 67]
i = 0
while i < len(arr) - 1:
    j = 0
    while j < len(arr) - 1 - i:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        j += 1
    i += 1
print(arr)