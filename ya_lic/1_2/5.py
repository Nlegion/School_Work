# Добавьте в предыдущую программу возможность вместо «раз» ввести «один».

x = input()
y = input()
z = input()
if ((x == 'раз') or (x == 'один')) and (y == 'два') and (z == 'три'):
    print("ГОРИ")
else:
    if (x == '1') and (y == '2') and (z == '3'):
        print("ГОРИ")
    else:
        print("НЕ ГОРИ")
