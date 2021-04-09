# Вывести степень заданного числа. цикл While обязателен
# число и степень задаем сами
# например: 2 в степени 3  = 2*2*2 = 8
num = int(input('Введите число'))
step= int(input('Введите степень'))
item = 1
result = 1
while item <= step:
    result = num * result
    print(item,'степень чиcла',num,'=',result)
    item += 1