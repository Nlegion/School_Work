# Из передачи “Здоровье” Аня узнала, что рекомендуется
# спать хотя бы AA часов в сутки, но пересыпать
# тоже вредно и не стоит спать более BB часов.
# Сейчас Аня спит HH часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям
# передачи “Здоровье”, выведите “Это нормально”.
# Если Аня спит менее AA часов, выведите “Недосып”,
# если же более BB часов, то выведите “Пересып”.

# пример данных AA = 6 BB = 10 HH = 8
a = int(input('рекомендуется спать'))
b = int(input('не стоит спать более'))
h = int(input('Сейчас Аня спит HH'))

if h < a:
    print('Недосып')
elif h > b:
    print('Пересып')
else:
    print('Это нормально')