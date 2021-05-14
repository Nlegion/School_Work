#Дан список стран и городов каждой страны.
# Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

#Russia Moscow Petersburg Novgorod Kaluga
#Ukraine Kiev Donetsk Odessa

x = 'Odessa' #input('введите город')
cont = {
    'Moscow' : 'Russia',
    'Petersburg' : 'Russia',
    'Novgorod' : 'Russia',
    'Kaluga' : 'Russia',
    'Kiev' : 'Ukraine',
    'Donetsk' : 'Ukraine',
    'Odessa' : 'Ukraine',
    }
print(cont[x]) # вывод по ключу
print(cont) # вывод всего словаря
print(cont.keys()) # вывод ключей
print(cont.values()) # значение
print(cont.items()) # ключ - значение

