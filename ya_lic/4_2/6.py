# Сделать снежинки на изображении полупрозрачными, чтобы через них просвечивался фон, можно смешав компоненты цвета снежинки и фона в какой-нибудь пропорции. Например, 80% снежинки и 20% фона:
#
# r = int(r1 * 0.8 + r2 * 0.2)
# В файле forest.png находится фон, а в файле snow.png – снежинка.
# Напишите функцию snow_forest(), которая принимает координаты верхнего левого угла, в который нужно вставить снежинку, уменьшенную до размера 100х100, и процент цвета снежинки, который нужно оставить.
# Полученное изображение нужно сохранить в файл output.png.
#
# Формат ввода
# Пример вызова:
# snow_forest((450, 300), 30)