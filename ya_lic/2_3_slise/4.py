# Формат телефонного номера в США обычно такой: сначала идет +1, затем 10 цифр, разделенных скобками и дефисами по 3 или 4:
# +1(XXX)XXX-XXXX

a, b = input(), int(input())

while True:
    if len(a) != 0:
        print(a[-b:])
        a = a[:(len(a) - b if len(a) - b > 0 else 0)]
    if len(a) != 0:
        print(a[:b])
        a = a[b:]
    if len(a) == 0:
        break
