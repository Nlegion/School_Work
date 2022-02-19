import story

# Урок 1. Знакомство
# Изучаемый материал print, input, переменная, текст, строка, f строка
print(story.edu())
print("Привет! Добро пожаловать в образовательный квест!")
print("Перед тем как мы начнем, Представься!")

hero_name = input('введите имя героя:')
hero_race = input('к какому народу герой принадлежит?')
hero_class = input('профессия героя?')
hero_age = int(input('сколько герою лет?'))

print(story.story_text(hero_name, hero_class, hero_race, hero_age))
