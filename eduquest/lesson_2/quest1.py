print('Вы находитесь в пещере на развилке. ',
      '\nВы можете пойти "налево", "направо" или "прямо".')
room = input('Введите одно из слов в кавычках для выбора.')
if room not in ('налево', 'направо', 'прямо'):
    exit(0)
elif room == 'налево':
    print('вы пошли налево, перед вами две двери, в какую вы пойдете(введите номер двери)?')
    door = input()
    if door not in ('1', '2'):
        exit(0)
    elif door == '1':
        print('Вы вышли из подземелья!')
    elif door == '2':
        print('Вы проволились в огромную яму и умерли с голода')
if room == 'направо':
    print('Вы пошли направо, перед вами две двери, в какую вы пойдете(введите номер двери)?')
    door = input()
    if door not in ('1', '2'):
        exit(0)
    elif door == '1':
        print('Вы нашли ультра редкий предмет ничего')
    elif door == '2':
        print('Вы нашли сокровища')
if room == 'прямо':
    print('Вы пошли прямо, перед вами две двери, в какую вы пойдете(введите номер двери)')
    door = input()
    if door not in ('1', '2'):
        exit(0)
    elif door == '1':
        print('Перед вами две двери какую выберите?')
        door = input()
        if door not in ('1', '2'):
            exit(0)
        elif door == '1':
            print('Вы нашли комнату с никогда не спящим существом по имени программист')
        elif door == '2':
            print('Вы нашли самопишущую клавиатуру')
    elif door == '2':
        print('Вы нашли комнату с человеком который сейчас сидит и пишет этот код')