#Даны два целых числа A и В.
#Выведите все числа от A до B включительно,
#в порядке возрастания, если A < B,
#или в порядке убывания в противном случае.
a = int(input('введите число А'))
b = int(input('введите число Б'))
if a <= b:
    for item in range(a, b):
        print(item)
else:
    #for item in range(b, a):
        #print(a-item)
    for item in range(a, b,-1):
        print(item)