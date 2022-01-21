import turtle as t

a = 100
b = 90
c = 0
t.shape('turtle')
t.speed(1)
t.pencolor('red')
while c <= 3:
    t.forward(a)
    t.left(b)
    c += 1
t.mainloop()
