import random
a = 0
rat_health = 10
spider_health = 20

print('Вы находитесь в пещере на развилке. ',
      '\nВы можете пойти "налево", "направо" или "прямо".')
room = input('Введите одно из слов в кавычках для выбора.')

if room not in ('налево', 'направо', 'прямо'):
    print('Ну и пожалуйста, ну и не нужно...')
    exit(0)
elif room == 'налево':
    print('На вас напала крыса!')
    battle = input("Атаковать крысу? да/нет")
    if battle == "да":
        while rat_health != 0:
            i = random.randint(1, 3)
            if i == 3:
                rat_health -= i
                print("Попал! Здоровье врага:", rat_health)
            elif i == 2:
                rat_health -= i
                print("Попал! Здоровье врага:", rat_health)
            elif i == 1:
                print("Промахнулся! Здоровье врага:", rat_health)
    else:
        print('Струсил? Убегаешь? да/нет')
        if input() == "да":
            exit(0)
        else:
            print('Тебе удалось убежать! Приключение продолжается!')

    print('вы пошли налево, перед вами две двери, в какую вы пойдете(введите номер двери)?')
    door = input()
    if door not in ('1', '2'):
        print('Ну и пожалуйста, ну и не нужно...')
        exit(0)
    elif door == '1':
        print('Вы вышли из подземелья!')
    elif door == '2':
        print('Вы проволились в огромную яму и умерли с голода')



if room == 'направо':
    print('Вы пошли направо, перед вами две двери, в какую вы пойдете(введите номер двери)?')
    door = input()
    if door not in ('1', '2'):
        print('Ну и пожалуйста, ну и не нужно...')
        exit(0)
    elif door == '1':
        print('Вы нашли ультра редкий предмет ничего')
    elif door == '2':
        print('Вы нашли сокровища')

if room == 'прямо':
    print('На вас напал Павук!')
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

    print('Вы пошли прямо, перед вами две двери, в какую вы пойдете(введите номер двери)')
    door = input()
    if door not in ('1', '2'):
        print('Ну и пожалуйста, ну и не нужно...')
        exit(0)
    elif door == '1':
        print('Перед вами две двери какую выберите?')
        door = input()
        if door not in ('1', '2'):
            print('Ну и пожалуйста, ну и не нужно...')
            exit(0)
        elif door == '1':
            print('Вы нашли комнату с никогда не спящим существом по имени программист')
        elif door == '2':
            print('Вы нашли самопишущую клавиатуру')
    elif door == '2':
        print('Вы нашли комнату с человеком который сейчас сидит и пишет этот код')
