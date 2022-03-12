# Помогите Золушке перебрать крупу, то есть выбрать из предложения только слова с указанной подстрокой.
#
# Формат ввода
# Вводится подстрока, затем строка слов через пробел.
#
# Формат вывода
# Выведите через пробел слова, в которых есть подстрока.
# Решите задачу в одну строку (не считая ввода и вывода).

p = input()
s = [x for x in list(input().split(' ')) if p in x]
print(' '.join(s))
