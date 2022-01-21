import turtle
turtle.speed(0)
turtle.shape('turtle')
t=0.1
for i in range(760):
    turtle.left(2)
    turtle.forward(t)
    t+=0.01
turtle.mainloop()