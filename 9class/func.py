def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
a = int (input('введте число А'))
b = int (input('введте число Б'))
c = input('введте действие + - * /')
if c == "+":
    print(addition(a, b))
elif c == "-":
    print(subtraction(a, b))
elif c == "*":
    print(multiplication(a, b))
else:
    print(division(a, b))
