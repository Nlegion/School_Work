# Помните?
#
# Варкалось. Хливкие шорьки
# Пырялись по нове,
# И хрюкотали зелюки,
# Как мюмзики в мове.
#
# Что за шорьки? Какие зелюки? Почему они хрюкочут? Или хрюкотают? Неизвестно, зато видно, что их много.
#
# Напишите программу, которая найдет в предложении существительное и число (записано цифрами) и согласует их между собой. Для некоторого упрощения из предложения убраны знаки препинания и все слова записаны с маленькой буквы.
#
# Формат ввода
# Вводятся строки, в которых через пробел записаны слова – среди них только одно существительное и только одно число.

import sys
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

inp = list(map(lambda x: x.replace('\n', ''), sys.stdin.readlines()))

for words in inp:
    words = words.split()
    sc = 0
    noun = ''
    for i in words:
        pr = morph.parse(i)
        for i2 in pr:
            if i2.tag.POS == 'NOUN' and i2.score > sc:
                noun = i2.word
                sc = i2.score

    num = int(list(filter(lambda x: x.isdigit(), words))[0])
    print(num, morph.parse(morph.parse(noun)[0].normal_form)[0].make_agree_with_number(num).word)
