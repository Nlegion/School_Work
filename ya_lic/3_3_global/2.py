# Напишите функцию prompter(), которая подсказывает строку по ее подстроке. Если аргумент функции есть в строке, которая уже встречалась при предыдущих вызовах функции, то возвращается строка целиком. Если нет, то возвращается просто аргумент функции.
#
# Пример
# Ввод	Вывод
# print(prompter("Why do you cry, Willy?"))
# print(prompter("Why, Willy?"))
# print(prompter("Why do"))
# Why do you cry, Willy?
# Why, Willy?
# Why do you cry, Willy?


q = []
w = ''


def prompter(line):
    global q, w
    q.append(w)
    w = line
    for i in q:
        if line in i:
            return i
    return line
