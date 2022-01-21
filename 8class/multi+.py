start = int(input('введите число'))
stop = int(input('введите число'))
step = int(input('введите число'))
for item in range(start,stop+1,step):
    print(end="")
    for item_2 in range(1,11,1):
      print(item, '*', item_2, '=',"{}    "
              .format(item * item_2), end="")
    print()
