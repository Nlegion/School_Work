# Зашифруйте введенную строку таким образом:
# разбить строку на две части пополам;
# записать новую строку так, чтобы символы из первой части чередовались символами из второй части.
#
# Если длина строки нечетная, то в первой части на 1 символ больше.
#
s = input()

i = 0
j = (len(s) + 1) // 2

a = ''
while i < (len(s) + 1) // 2:
    a += s[i]
    if j < len(s):
        a += s[j]
    i += 1
    j += 1
print(a)
