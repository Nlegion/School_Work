# апишите программу, выбирающую из текста глаголы и сортирующую их нормальную форму по виду: совершенный или несовершенный.
#
# Формат ввода
# Вводится текст.
#
# Формат вывода
# В отрывке произведения найдите все слова, среди возможных вариантов разбора которых есть глагол, выберите значение с наивысшим score, переведите его в нормальную форму и выведите без повторений сначала по виду (несовершенные, затем совершенные), затем внутри одного вида по алфавиту.
#
# Пример 1
# Ввод	Вывод
# Плывет, плывет кораблик
# На запад, на восток.
# Канаты — паутинки,
# А парус — лепесток.
#
# Соломенные весла
# У маленьких гребцов.
# Везет, везет кораблик
# Полфунта леденцов.
#
# Ведет кораблик утка,
# Испытанный моряк.
# — Земля! — сказала утка. —
# Причаливайте! Кряк!
# везти
# вести
# плыть
# причаливать
# сказать

import pymorphy2
import sys


def delete_marks(str_in):
    marks = '!.?,—:'
    ret_str = ''
    for x in str_in:
        if x in marks:
            continue
        else:
            ret_str += x
    return ret_str


def is_word_verb(word):
    return word.tag.POS == 'VERB' or word.tag.POS == 'INFN'


data = list(map(str.strip, sys.stdin))
morph = pymorphy2.MorphAnalyzer()
perf_list = set()
imperf_list = set()
for elem in data:
    elem_nom = delete_marks(elem)
    str_data = elem_nom.split()
    if len(str_data) == 0:
        continue
    for str_elem in str_data:
        word1 = morph.parse(str_elem)
        word1 = list(filter(is_word_verb, word1))
        if len(word1) == 0:
            continue
        word = word1[0]
        if (word.tag.POS == 'VERB' or word.tag.POS == 'INFN') and word.tag.aspect == 'perf':
            perf_list.add(word.normal_form)
        if (word.tag.POS == 'VERB' or word.tag.POS == 'INFN') and word.tag.aspect == 'impf':
            imperf_list.add(word.normal_form)
perf_list = list(perf_list)
imperf_list = list(imperf_list)
perf_list.sort()
imperf_list.sort()
imperf_list.extend(perf_list)
for elem in imperf_list:
    print(elem)