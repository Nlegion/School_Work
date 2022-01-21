import turtle as tu

def Koch(length):
    if length <= 2 :
        tu.fd(length)
        return
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)
    tu.rt(120)
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)


tu.speed(1000)
length = 300.0
tu.penup()
tu.backward(length/2.0)
tu.pendown()
Koch(length)
tu.done()