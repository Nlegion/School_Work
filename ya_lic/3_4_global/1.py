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

def extend_list(func):
    def wrapper(*args):
        wrapper.a.extend(*args)
        return func(wrapper.a)

    wrapper.a = []
    return wrapper


@extend_list
def refinement(lst):
    a = list(filter(lambda x: (not x % 2, x % 2)[sum(lst) % 2], lst))
    if len(a) != 0:
        return sum(a) / len(a)
    else:
        return 0