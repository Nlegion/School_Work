# Богат и могуч русский язык! Много в нем правил: как ударить, а где не ударять. Но сейчас нужно просто сосчитать количество безударных гласных в строке слов, записанных через произвольное количество пробелов. В начале и конце предложения пробелов нет.
#
# Формат ввода
# Вводится строка, в которой слова разделены одним или несколькими пробелами.
#
# Формат вывода
# Подсчитать количество безударных гласных в этой фразе.
# Гласные в русском языке: аяоёэеуюыи

vowel = 'аяоёэеуюыи'
stroka = input()
v = k = z = 0
n = 1
for w in stroka:
    if w in vowel:
        if n:
            z += 1
        k += 1
        n = 0
    elif w == ' ':
        n = 1
        if k:
            v += k
            k = 0
print(v - z + k)
