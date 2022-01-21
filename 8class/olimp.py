import itertools
from itertools import combinations
word  = '123456789'
word_2 = map(str,word)
new_word = []
num = 0
xor = 0
for item in word_2:
    if item not in new_word:
        new_word.append(item)
        num += 1


