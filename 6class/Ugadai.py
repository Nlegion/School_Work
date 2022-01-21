import random
ran = random.randint(1,100)
step = 0
while step <= 10:
    n = int(input ('Введите число от smht до 100'))
    if n == ran:
        print('Угадал')
        break
    elif n < ran:
        print('Нет) Ваше число меньше')
    elif n > ran:
        print('Нет) Ваше число больше')
    step += 1
