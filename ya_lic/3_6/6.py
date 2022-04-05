# Заменять можно много чего. Например, в схеме предложения нижнее подчеркивание заменяет слово. А черточка с вертикальной чертой спереди заменяет слово, начинающееся с большой буквы.
#
# Напишите функцию placeholder(), которая множество строк сортирует по заменителям.
#
# Функция принимает произвольное количество позиционных аргументов-строк и произвольное количество именованных аргументов, значениями которых являются схемы различных предложений. Слова заменены нижним подчеркиванием или вертикальной чертой с нижним подчеркиванием, знаки препинания стоят на своих местах.
#
# Функция возвращает словарь, ключи которого – схемы предложений, значения – списки предложений с такой схемой, отсортированные по алфавиту. Если для предложения нет подходящей схемы, оно никуда не записывается, если для схемы не нашлось предложений, такой ключ не создается.
#
# Пример
# Ввод	Вывод
# lines = ["Look at the boy, he has a toy.",
#          "Look at me.", "I am happy.",
#          "Here is the kitchen where Mother cooks for me.",
#          "What are little boys made of?",
#          "What are little girls made of?",
#          "Look at the girl, she has a doll."]
# holders = {"h1": "|_ _ _ _, _ _ _ _.",
#            "h2": "|_ _ _.", "h3": "|_ _ _ _ _ _?"}
# for k, v in placeholder(*lines, **holders).items():
#     print(k, "->", *v)
# |_ _ _ _, _ _ _ _. -> Look at the boy, he has a toy. Look at the girl, she has a doll.
# |_ _ _. -> I am happy. Look at me.
# |_ _ _

def placeholder(*args, **kwargs):
    res = {}
    for line in args:
        tmp = ''.join(map(lambda x: '|_' if x.isupper() else '_' if x.isalpha() else x, line))
        while '__' in tmp:
            tmp = tmp.replace('__', '_')
        for value in kwargs.values():
            if tmp == value:
                res[value] = res.get(value, []) + [line]
    return {k: sorted(v) for k, v in res.items()}
