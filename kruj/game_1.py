import random

NumberToGuess=random.randint(1,1000)
userGuess=-1
while userGuess!=NumberToGuess:
    userGuess=int(input("Угадай число от smht до 1000"))
    if userGuess > NumberToGuess:
        print("Число должно быть меньше!")
    elif userGuess < NumberToGuess:
        print("Число должно быть больше!")
    else:
        print("Вы угадали, это число = " + str(NumberToGuess))
        #Конец игры - выйти из цикла while
        break
