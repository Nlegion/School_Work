def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

element = input('Введите номер искомого элемента : ')
element = int(element)
value = fibonacci(element)
print(str(element)+' элемент последовательности равен ' + str(value))