# Любой мир фэнтези начинается с карты с городами, замками, крепостями, между которыми потом будут путешествовать персонажи. Чтобы все выглядело натуральным, нужно все эти населенные пункты разместить на карте случайным образом. И пусть их размеры и население тоже будут случайными, но в разумных пределах.
#
# Напишите функцию generate_fandom(n, names), которая создает n городов, выбирая случайное название из предложенного списка names (все имена должны быть уникальны). А также их параметры:
# размер – случайное число из диапазона 10 – 20, повторения возможны;
# население – случайное число, кратное 10000, из диапазона 10000 – 1000000, повторения возможны;
# расстояние от метрополии – случайное число из диапазона 100 – 500, без повторений.
#
# Функция возвращает список кортежей из названия, размера, населения и расстояния для каждого города. Числа целые, концы диапазонов включаются.
#
# Пример
# Ввод	Вывод
# names = ['Ankh-Morpork', 'Twin Peaks', 'Atlantis', 'Springfield', 'Zion']
# for item in generate_fandom(3, names):
#     print(*item)
# Ankh-Morpork 19 640000 301
# Twin Peaks 13 690000 337
# Springfield 13 960000 333

from random import randrange, randint, sample


def generate_fandom(n, names):
    it = []
    ss = []
    i = 0
    while i < n:
        name = sample(names, k=1)
        if name not in it:
            s = randint(10, 20)
            nn = randrange(10000, 1000000, 10000)
            rr = sample(range(100, 500), 1)
            it.append(name)
            ss.append(name + [s] + [nn] + rr)
            i += 1
    return ss