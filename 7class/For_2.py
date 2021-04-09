import turtle as t # переименовать библиотеку в t
import time
t.reset()
t.speed(10)
t.pensize(3)
for row in range(10):
    for column in range(10):
        for square in range(6):
            t.fd(20)
            t.left(60)
        t.penup()
        t.fd(35)
        t.pendown()
    t.penup()
    t.left(180)
    t.fd(190)
    t.right(90)
    t.fd(35)
    t.right(90)
    t.pendown()
time.sleep(10)
