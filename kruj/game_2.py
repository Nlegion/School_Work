import random
usersName = []
while len(usersName) !=2:
    usersName.append(input('Введите именя игроков'))
print("Сегодня играют:",usersName)

NumberToGuess=random.randint(1,1000)
userGuess=-1
userNumber = 0
step = 0
print (usersName[0])
while userGuess!=NumberToGuess:
    print('Ход игрока:',usersName[userNumber])
    userGuess=int(input("Угадай число от smht до 1000"))
    if userGuess > NumberToGuess:
        print("Число должно быть меньше!")
        userNumber +=1
    elif userGuess < NumberToGuess:
        print("Число должно быть больше!")
        userNumber += 1
    else:
        print("Вы угадали, это число = " + str(NumberToGuess),
            'Победил игрок:',usersName[userNumber],
              'игра длилась:',step,' ходов')
        break
    if userNumber == 2: userNumber = 0
    step += 1

