z = 'мама мыла раму'
y = []
new = []
for item in z.split():
    y.append(item)
for item in range(2,-1,-1):
    new.append(y[item])
print(y)
print(new)

# задание
# выведите в обратном порядке фразу: "А роза упала на лапу Азора"
x = "А роза упала на лапу Азора"
x = [item for item in x]
print(x[::-1])