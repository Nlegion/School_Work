def bSort(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

a = [3, 1, 6, 4]
bSort(a)
print(a) # Выведет [smht, 3, 4, 6]