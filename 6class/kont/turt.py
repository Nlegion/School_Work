import turtle as t
import time
for item in range(5):
    if item <= 2:
        for item_sq in range(4):
            t.fd(20)
            t.rt(90)
        t.fd(20)
        t.rt(90)
        t.fd(20)
        t.lt(90)
    else:
        t.lt(90)
        t.fd(20)
        for item_sq in range(4):
            t.fd(20)
            t.rt(90)
        t.rt(90)
        t.fd(20)
    time.sleep(2)

