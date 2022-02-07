import random

a = 0
rat_health = 10
spider_health = 20

print ('На вас напала крыса!')
battle= input("Атаковать крысу? да/нет")
if battle == "да":
    while rat_health != 0:
        i = random.randint(1, 3)
        if i == 3:
            rat_health -= i
            print("Попал! Здоровье врага:",rat_health )
        elif i == 2:
            rat_health -= i
            print("Попал! Здоровье врага:",rat_health)
        elif i == 1:
            print("Промахнулся! Здоровье врага:", rat_health)
else:
    print('Струсил? Убегаешь? да/нет')
    if input() == "да":
        exit(0)
    else:
        print('Тебе удалось убежать! Приключение продолжается!')

print ('На вас напал Павук!')
battle = input("атаковать? да/нет")
if battle == "да":
    while spider_health != 0:
        f = random.randint(1, 2)
        if f == 2:
            spider_health -= f
            print("Попал! Здоровье врага:", spider_health)
        elif f == 1:
            print("Промахнулся! Здоровье врага:", spider_health)
else:
    print('Струсил? Убегаешь? да/нет')
    if input() == "да":
        exit(0)
    else:
        print('Тебе не удалось убежать!')
        exit(0)
