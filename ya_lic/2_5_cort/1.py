# Формат ввода
# Вводятся целые числа, пока не будет введен ноль.
#
# Формат вывода
# Выведите их в порядке убывания, но без последнего нуля (Ахиллес, по апории, черепаху не догнал). Выводить через ->
#
# В задаче нельзя пользоваться стандартной сортировкой.

z = 1
y = set()
while z != 0:
    z = int(input())
    if z != 0:
        y.add(z)
nums = list(y)
n = 1
while n < len(nums):
    for i in range(len(nums) - n):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    n += 1
for item in list(nums)[::-1]:
    if item != min(nums):
        print(str(item) + '->', end='')
    else:
        print(str(item), end='')
