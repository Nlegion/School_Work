# Если числа имеют среди делителей только 2, 3 и 5 в любой степени, то, расположенные по возрастанию, они образуют последовательность Хэмминга. Выведите n-е число последовательности.
#
# Первые 10 чисел такие: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.

def is_hamming_numbers(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return is_hamming_numbers(x / 2)
    if x % 3 == 0:
        return is_hamming_numbers(x / 3)
    if x % 5 == 0:
        return is_hamming_numbers(x / 5)
    return 0


n = int(input())
c = 0
num = 2

while c < n:
    if is_hamming_numbers(num):
        c += 1
    num += 1
print(num - 1)
