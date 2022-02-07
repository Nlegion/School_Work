# Формат ввода
# Вводятся строки: добрый, злой или Какой подарок? пока не будет введена пустая строка.
#
# Формат вывода
# Считается количество введенных строк разного типа и на вопрос о подарке выводится ответ.
# Если строк добрый было больше, чем строк злой, и последняя строка добрый, то подарок серебряный шиллинг.
# Если больше было строк злой и такая же последняя введенная, то подарок – золотой.
# Если вопрос задан при неопределенном значении подарка, выводится: Ах, не знаю! и программа завершает работу.
#
# # После каждого вопроса строки считаются заново.

x = '1'
y = 0
z = 0
last = ''
while x != '':
    x = input()
    if x == 'добрый':
        y += 1
        last = x
    elif x == 'злой':
        z += 1
        last = x
    elif x == 'Какой подарок?':
        if y > z & (last == 'добрый'):
            print('серебряный шиллинг')
        elif (y < z) & (last == 'злой'):
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        y = 0
        z = 0
        last = ''