import turtle as t # использовать библиотеку как t
import time

t.reset() # начать заново (обнулить параметры)
t.speed(10) # скорость выполнения  от smht (медленно) до 100 (быстро)
t.pensize(3) # размер линии
for item in range(5): # цикл с количеством действий, item  - переменная счетчик (№ текущего шага)
    if item <= 2: # ветвление (проверка количества шагов)
        for sq in range(4):
            t.fd(20) # вперед (кол-во пикселей вперед)
            t.rt(90) # поворот вправо на 90 градусов
        t.fd(20)  # вперед (кол-во пикселей вперед)
        t.rt(90)  # поворот вправо на 90 градусов
        t.fd(20)  # вперед (кол-во пикселей вперед)
        t.lt(90)  # поворот влево на 90 градусов
    else:
        t.lt(90)  # поворот влево на 90 градусов
        t.fd(20)
        for sq in range(4):
            t.fd(20) # вперед (кол-во пикселей вперед)
            t.rt(90) # поворот вправо на 90 градусов
        t.rt(90)  # поворот влево на 90 градусов
        t.fd(20)
    time.sleep(2) # стоп на 2 сек