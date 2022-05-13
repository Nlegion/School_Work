# А теперь нужно написать еще одну функцию – little_green_men_names(m, n) – возвращающую список из m неповторяющихся имен маленьких зеленых человечков из планетной системы
# α
# −
# ω
# −
# F
# o
# m
# a
# l
# g
# a
# u
# t
# −
# 4
#  (Альфа-Омега-Фомальгаут-4) длины n.
# Решение должно содержать две функции: name(n) – создающую случайное имя длиной n, и little_green_men_names(m, n) – создающую m неповторяющихся имен длины n.
# Правила создания имени прежние:
# – имя должно состоять из двух частей, то есть содержать один пробел; первая часть не может быть короче 2 символов, вторая может состоять из одного символа;
# – в первой части обязательно должна быть цифра, но она не должна стоять на первом месте; остальные символы могут быть буквами латинского алфавита в любом регистре или цифрами;
# – вторая часть должна начинаться с буквы из первой половины латинского алфавита в верхнем регистре; остальные символы могут быть любыми буквами латинского алфавита в нижнем регистре;
# – символы без учета регистра в имени не повторяются.
#
# Формат вывода
# Например, при вызове функции
# print(*little_green_men_names(10, 12), sep=’\n’)
#
# может получиться такой вывод:
#
# H5 Dtijlwagq
# Feb9 Klwqycn
# p2m Dihlsuvz
# b1 Lcxqkzmju
# Ci2e Gqhrkaj
# e8 Cgzrvptko
# k9R1qtv6 Jiy
# q8w2p Cbdovr
# pRVWGxyL4 Jf
# VU85KEc0FI A

import string
from random import randint

symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits


def get_unique(start, end, nlst):
    lst = nlst
    symbol = symbols[randint(start, end)]
    while (symbol in lst) or (symbol.swapcase() in lst):
        symbol = symbols[randint(start, end)]
    return symbol


def name(n):
    # Первая часть
    x = randint(2, n - 2)  # Длина не меньше 2
    symb = symbols[randint(0, 51)]
    name = [symb]  # Первый символ - любая буква
    for i in range(x - 2):
        name.append(get_unique(0, 61, name))  # Заполняем "хвост" любыми символами
    name.insert(randint(1, x - 1), get_unique(52, 61, name))  # Обязательная цифра в любое место, кроме первого

    name.append(' ')  # Пробел между частями

    # Вторая часть
    name.append(get_unique(0, 12, name))  # Прописная буква из первой половины латиницы
    for i in range(n - x - 2):
        name.append(get_unique(26, 51, name))  # Заполняем "хвост" строчными символами латиницы
    return ''.join(name)


def little_green_men_names(m, n):
    return [name(n) for _ in range(m)]
