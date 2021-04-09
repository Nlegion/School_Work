def sum(a,b):
    return print(a+b)
def dif(a,b):
    return print(a-b)
def div(a,b):
    return print(a/b)
def prod(a,b):
    return print(a*b)

a = float(input())
b = float(input())
c = input('+ - / *')
if c == '+':
    sum(a,b)
elif c == '-':
    dif(a,b)
elif c == '/':
    div(a,b)
else:
    prod(a,b)