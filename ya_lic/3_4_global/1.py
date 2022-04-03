# Накопление новых данных иногда приводит к пересмотру исходной гипотезы.
#
# Напишите функцию refinement(), которая будет уточнять вывод после каждого вызова.
# Функция вызывается с аргументом – списком чисел, которые дополняют числа из прошлых вызовов. Возвращается значение – среднее арифметическое чисел, имеющих ту же четность, что и сумма всех данных при всех вызовах функции. Если таких данных не оказалось, возвращается 0.
#
# Пример
# Ввод	Вывод
# print(refinement([1, 2, 3]))
# print(refinement([4, 5, 6, 7]))
# print(refinement([1]))
# 2.0
# 4.0
# 3.4
# Примечания
# В задаче нельзя использовать инструкцию global.

