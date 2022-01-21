def mul (a,b):
    return a*b
def min(a,b):
    return a-b
def plu (a,b):
    return a+b
def div (a,b):
    return a/b

x = int(input('введите число А'))
y = int(input('введите число Б'))
user = input('* , / , + , -')

if user == '*':
    print(mul(x,y))
elif user == '/':
    print(div(x,y))
elif user == '+':
    print(plu(x,y))
else:
    print(min(x,y))