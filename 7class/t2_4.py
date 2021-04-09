def sum(a, b):
    return (a+b)
def minu(a, b):
    return (a-b)
def uni(a, b):
    return (a*b)
def divi(a, b):
    return (a/b)

a=float(input('введите первое число'))
b=float(input('введите второе число'))
сalc=str(input('введите действие'))
if сalc == '+':
    print(sum(a, b))
elif сalc == '-':
    print(minu(a, b))
elif сalc == '*':
    print(uni(a, b))
else:
    print(divi(a, b))