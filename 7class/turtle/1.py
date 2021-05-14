import turtle as t
import time

t.speed(10)
t.pensize(2)
t.pencolor('green')

size_side = 30
obtuse_angle = 45
acute_angle = 180 - obtuse_angle

for item in range(2):
    t.lt(acute_angle)
    t.fd(size_side)
    t.lt(obtuse_angle)
    t.fd(size_side)
t.penup()
t.fd(size_side)
t.lt(180)
t.pendown()

for item in range(2):
    t.rt(acute_angle)
    t.fd(size_side)
    t.rt(obtuse_angle)
    t.fd(size_side)

time.sleep(10)