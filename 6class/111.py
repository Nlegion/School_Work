x = int(input())
z = 0
y = 0
while x > 0:
    z = x % 10
    x = x // 10
    if z <= y:
        print('no')
        break
    else:
        print('yes')