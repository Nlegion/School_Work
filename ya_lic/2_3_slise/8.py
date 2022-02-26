# В научных текстах принято ссылаться на источники, указывая их или ссылки на них в квадратных скобках после текста.
# Напишите программу, которая удалит из текста все ссылки на источники цитирования, то есть текст, записанный в квадратных скобках. Ну и сами скобки заодно. Внутри скобок могут быть еще скобки.
#
# Пример
# Ввод	Вывод
# My family[Jerald Darrell[1]] and other animals[2]
# My family and other animals

text = input()
stack = []
text_new = ""
for ch in text:
    if ch == "[":
        stack.append(ch)
    if ch == "]":
        stack.pop()
    else:
        if len(stack) == 0:
            text_new += ch
            # print(ch)

print(text_new)
