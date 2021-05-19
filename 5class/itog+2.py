a = 100
b = 'Строка'
print('a=',a,'b=',b)

z = a
a = b
b = z
print('a=',a,'b=',b)

a,b = b,a
print('a=',a,'b=',b)