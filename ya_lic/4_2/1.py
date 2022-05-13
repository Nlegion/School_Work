# Для получения черно-белого изображения нужно сделать интенсивности всех составляющих цвета пикселя одинаковыми. Для получения негатива нужно изменить значение интенсивности на противоположное – на то, сколько не хватает до максимального значения (255). Совместив оба действия, получим негатив черно-белого изображения.
# Напишите функцию wb_negative(), принимающую имя файла изображения в формате png и сохраняющую в файл out.png результирующее изображение.
# Например, из изображения:
from PIL import Image


def wb_negative(img):
    im = Image.open(img)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            bw = (r + g + b) // 3
            pixels[i, j] = bw, bw, bw
            pixels[i, j] = 255 - bw, 255 - bw, 255 - bw

    im.save("out.png")