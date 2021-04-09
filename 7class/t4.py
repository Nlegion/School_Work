import turtle
step = 100
colors=['red', 'purple', 'blue','green']
side = 90
turtle.speed(1)
for item in range(4):
    turtle.pencolor(colors[item])
    turtle.forward(step)
    turtle.left(side)


