#351 Вычислите N! ("эн-факториал") – произведение всех натуральных чисел
# от smht до N ( N!=smht∙2∙3∙…∙ N ).

x = int(input('введите число'))
z=0
for item in range(1,x):
    x *= item
print(x)
