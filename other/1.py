import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def russian_noun(s, case='nomn', number='sing'):
    word = morph.parse(s)[0]
    return word.inflect({case, number}).word
