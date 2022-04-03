# Напишите функцию numerals() для записи чисел до 100 словами на английском языке.
#
# Пример 1
# Ввод	Вывод
# print(numerals(30))
# thirty
# Пример 2
# Ввод	Вывод
# print(numerals(99))
# ninety-nine

one = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
       6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
       11: 'eleven', 12: 'twelve', 13:
           'thirteen', 14: 'fourteen', 15: 'fifteen',
       16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 0: ''}
two = {2: 'twenty', 3: ' thirty', 4: 'forty', 5: 'fifty',
       6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 10: ''}


def numerals(s):
    if 0 < s < 20:
        answ = (one[s])
    elif 100 > s > 19:
        answ = (two[s // 10] + '-' + one[s % 10]) if one[s % 10] else two[s // 10]
    elif 1000 > s > 99:
        if -1 < (s % 100) < 20:
            answ = (one[s // 100] + '-' + 'hundred' + one[s % 100])
        else:
            answ = (one[s // 100] + '-' + 'hundred' + two[s % 100 // 10] + ' ' + one[s % 10])
    else:
        return 'zero'
    answ = ' '.join(answ.split())
    return answ

