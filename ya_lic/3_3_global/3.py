# Напишите функцию diversity(), которая при каждом вызове возвращает, сколько раз она уже вызывалась именно с этим аргументом.
#
# Пример
# Ввод	Вывод
# print(diversity("Happy"))
# print(diversity("New"))
# print(diversity("Year"))
# print(diversity("Year"))
# print(diversity("Year"))
# 1
# 1
# 1
# 2
# 3
# История решений

def args_counter():
    res = {}

    def inner(arg):
        res[arg] = res.get(arg, 0) + 1
        return res[arg]

    return inner


diversity = args_counter()