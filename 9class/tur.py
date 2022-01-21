import turtle as t
a = 100
b = 90
t.shape('turtle')
t.pencolor('green')
t.speed(1)
for item in range(4):
    t.forward(a)
    t.left(b)
t.mainloop()
