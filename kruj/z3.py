import turtle as t

a = 20
b = 90
c = 0
z = 4
t.shape('turtle')
t.speed(100)
t.pencolor('red')
for item in range(z):
    while c <= 3:
        t.forward(a)
        t.left(b)
        c += 1
    t.penup()
    t.forward(a*2)
    t.pendown()
    c = 0
t.mainloop()
