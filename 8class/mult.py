doit = int(input('введите число'))
for item in range(doit+1):
    print(end="")
    for item_2 in range(doit+1):
      print(item, '*', item_2, '=',"{}    "
              .format(item * item_2), end="")
    print()

