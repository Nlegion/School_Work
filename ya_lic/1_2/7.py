# Формат ввода
# Вводится строка.
#
# Формат вывода
# Если введено число от 5 до 10, то вывести Утро, от 11 до 17, то День, с 18 до 22 – Вечер, с 23 до 4 – Ночь.
# Если введено неверное число или слово, то вывести: Ошибка.

time = input()
if ('5' == time) or ('6' == time) or ('7' == time) or ('8' == time) or ('9' == time) or ('10' == time):
    print('Утро')
elif ('11' == time) or ('12' == time) or ('13' == time) or ('14' == time) or ('15' == time) or ('16' == time) or (
        '17' == time):
    print('День')
elif ('18' == time) or ('19' == time) or ('20' == time) or ('21' == time) or ('22' == time):
    print('Вечер')
elif ('23' == time) or ('0' == time) or ('1' == time) or ('2' == time) or ('3' == time) or ('4' == time):
    print('Ночь')

else:
    print('Ошибка')
