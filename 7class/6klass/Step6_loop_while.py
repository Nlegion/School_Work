user_list = []

while True:
    x = input('введите товар')
    if x == 'стоп':
        break
    else:
        user_list.append(x)
print(user_list)