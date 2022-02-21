# Помните, как в Алисе в стране чудес песенка Мыши изгибалась точно так же, как мышиный хвост? Напишите программу, имитирующую такое поведение слов.
#
# Вашей программу на вход подается сначала число – ширина поля, в которое должна поместиться песенка, гарантируется, что ширина не меньше самого длинного введенного слова.
#
# Затем вводится число – количество слов, затем сами слова.
#
# Слова нужно вывести в том же порядке таким образом, чтобы первое было написано слева без отступа, следующее сдвинуто пробелом на 1 позицию вправо, следующее еще на одну и так далее, пока очередное слово правым краем не достигнет границы. Тогда следующее слово начинаем сдвигать в обратную сторону на одну позицию справа, пока не достигнем левой границы началом слова. Пробелы в конце строк не ставятся, сдвиг слова достигается добавлением пробелов только с левой стороны от него.

max_length = int(input())
number_of_words = int(input())
up = True
down = False
add_gaps = False
word = input()
previous_length = len(word)
counter_of_gaps = 0
counter_of_words = 0

for i in range(number_of_words):
    counter_of_words += 1
    if i == 0:
        print(word)
        counter_of_gaps += 1
    else:
        if up:
            if add_gaps:
                counter_of_gaps += 1
                add_gaps = False
            if len(counter_of_gaps * " " + word) < max_length:
                print(counter_of_gaps * " " + word)
                counter_of_gaps += 1
                if len(counter_of_gaps * " " + word) == max_length:
                    counter_of_gaps -= 1
                    add_gaps = True
            else:
                up = False
                counter_of_gaps = max_length - len(word)
                print(counter_of_gaps * " " + word)
        if down:
            length = previous_length - 1
            counter_of_gaps = length - len(word)
            print(counter_of_gaps * " " + word)
            if counter_of_gaps <= 0:
                up = True
                down = False
                counter_of_gaps = 1
    if not up:
        down = True
    previous_length = len(counter_of_gaps * " " + word)
    if counter_of_words == number_of_words:
        break
    word = input()
    if word == "":
        break
