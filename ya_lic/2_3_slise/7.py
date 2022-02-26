# Даны две строки. Можно ли первую строку получить из второй циклическим сдвигом?
# Если можно, то выведите, на сколько позиций нужно сдвинуть вторую строку влево. Если нет, выведите NO.

# st1 = input()
# st2 = input()

st1 = 'сосна'
st2 = 'насос'
step = 0
while step < len(st1):
    if st2 == (st1[len(st1) - step::] + st1[:len(st1) - step:]):
        print(step)
        break
    step += 1
    if step == len(st1):
        print('NO')
        break
