import turtle
step = 100
colors=['red', 'purple', 'blue','green']
side = 90
turtle.speed(1)
for num in range(4):
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.pencolor(colors[num])
    for item in range(4):
        turtle.forward(step)
        turtle.left(side)


