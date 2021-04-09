arr = [1,2,41,454,23,65,87,234,567,234,63, 80, 62, 69, 71, 37, 12, 90, 19, 67]

def func_1 (arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(func_1(arr))

