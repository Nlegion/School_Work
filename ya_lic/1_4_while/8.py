# Вася не очень "дружит" с дробями. Но понимает: для того, чтобы их вычитать или складывать, нужно сначала привести к общему знаменателю. Помоги Васе написать программу, которая не только может вычесть две несократимые дроби, но и выведет результат в несократимом виде.
#
# Формат ввода
# На вход подается 4 числа: числитель и знаменатель первой дроби, затем числитель и знаменатель второй дроби.
#
# Формат вывода
# Выводится строка: числитель результата/знаменатель результата в несократимом виде.
#
delitel = 1
fraction_1 = 0
fraction_2 = 0
numerator_1 = int(input())
denominator_1 = int(input())
numerator_2 = int(input())
denominator_2 = int(input())
numerator_11 = numerator_1 * denominator_2
denominator_11 = denominator_1 * denominator_2
numerator_22 = numerator_2 * denominator_1
denominator_22 = denominator_2 * denominator_1
fraction_1 = numerator_11 - numerator_22
fraction_2 = denominator_1 * denominator_2
# print(fraction_1, "/", fraction_2)
if fraction_1 > fraction_2:
    min = fraction_2
else:
    min = fraction_1
while min >= 1:
    if fraction_1 % min == 0 and fraction_2 % min == 0:
        delitel = min
        fraction_1 = fraction_1 // delitel
        fraction_2 = fraction_2 // delitel
        break
    min -= 1
print(f'{fraction_1}/{fraction_2}')
