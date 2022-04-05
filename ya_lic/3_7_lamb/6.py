# Используя списочное выражение напишите функцию smart_search(), которой передается произвольное количество аргументов и функция для отбора (именованный аргумент func). Если переданные аргументы – целые числа, то функция возвращает кортеж из элементов, отобранных по условию в func. Если это строки, то возвращается кортеж из строк, начинающихся с прописной буквы. Гарантируется, что аргументы только числа или строки.
#
# Пример 1
# Ввод	Вывод
# print(smart_search(1, 2, 3, 5, 12, func=lambda x: x % 2))
# (1, 3, 5)
def smart_search(*li, func):
    if type(li[0]) == str:
        return tuple(i for i in li if i[0].isupper())
    return tuple(i for i in li if func(i))