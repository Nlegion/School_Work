# – Вы продаете рыбов?
# – Котам нет, у вас все равно денег нет.
# – Денег нет, а мыши есть. Поменяете рыбов на мышов?
#
# Напишите рекурсивную функцию change(line, sub, symb) для замены всех вхождений символа sub в строке line на символ symb.
#
# Метод replace использовать нельзя. Использование рекурсии обязательно.
#
# Пример 1
# Ввод	Вывод
# text = "abracadabra"
# print(change(text, "a", "o"))
# obrocodobro
def change(line, sub, symb):
    if line == '':
        return ''
    elif line[0] == sub:
        return symb + change(line[1:], sub, symb)
    else:
        return line[0] + change(line[1:], sub, symb)