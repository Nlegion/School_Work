# Минус, рожица кривая.
# Палка, палка, огуречик,
# Вот и вышел человечек.
# Нарисуйте человечка по образцу. Для этого нужно написать функцию human(), принимающую цвет фона, цвет линии, масштаб – размер одной клетки изображения в пикселях – и толщину линии. Нужно на полотне 16х21 клетку нарисовать человечка в указанном на рисунке масштабе. Клетки и дополнительные построения изображать не нужно. Полученную картинку сохранить в файл human.png.
# Как построить и расположить рот человечка, поясняется на врезке слева (квадрат со стороной 4 клетки, верхний левый угол в точке (клетка, пол клетки)). Каждый сустав и глаза человечка – это круг радиуса 1/5 от размера клетки (деление нацело), суставы не залиты, глаза залиты.

from PIL import Image, ImageDraw


def human(fcol, lcol, k, lw):
    im = Image.new("RGB", (16 * k, 21 * k), fcol)
    draw = ImageDraw.Draw(im)
    draw.ellipse((6 * k, 1 * k, 10 * k, 5 * k), width=lw, outline=lcol)  # голова
    draw.ellipse((7 * k - k // 5, 3 * k - k // 5, 7 * k + k // 5, 3 * k + k // 5), fill=lcol, width=lw,
                 outline=lcol)  # левый глаз
    draw.ellipse((9 * k - k // 5, 3 * k - k // 5, 9 * k + k // 5, 3 * k + k // 5), fill=lcol, width=lw,
                 outline=lcol)  # правый глаз
    draw.arc((6 * k, 1 * k - k // 2, 10 * k, 5 * k - k // 2), 45, 45 + 90, width=lw, fill=lcol)  # рот
    # плечи
    draw.ellipse((7 * k - k // 5, 6 * k - k // 5, 7 * k + k // 5, 6 * k + k // 5), width=lw, outline=lcol)
    draw.ellipse((9 * k - k // 5, 6 * k - k // 5, 9 * k + k // 5, 6 * k + k // 5), width=lw, outline=lcol)
    draw.line((7 * k, 6 * k, 9 * k, 6 * k), width=lw, fill=lcol)
    # тело
    draw.ellipse((8 * k - k // 5, 11 * k - k // 5, 8 * k + k // 5, 11 * k + k // 5), width=lw, outline=lcol)
    draw.line((8 * k, 5 * k, 8 * k, 11 * k), width=lw, fill=lcol)
    # левая рука
    draw.ellipse((4 * k - k // 5, 10 * k - k // 5, 4 * k + k // 5, 10 * k + k // 5), width=lw, outline=lcol)
    draw.line((4 * k, 10 * k, 7 * k, 6 * k), width=lw, fill=lcol)
    draw.line((4 * k, 10 * k, 6 * k, 13 * k), width=lw, fill=lcol)
    # правая рука
    draw.ellipse((12 * k - k // 5, 10 * k - k // 5, 12 * k + k // 5, 10 * k + k // 5), width=lw, outline=lcol)
    draw.line((9 * k, 6 * k, 12 * k, 10 * k), width=lw, fill=lcol)
    draw.line((12 * k, 10 * k, 15 * k, 7 * k), width=lw, fill=lcol)
    # левая нога
    draw.ellipse((6 * k - k // 5, 15 * k - k // 5, 6 * k + k // 5, 15 * k + k // 5), width=lw, outline=lcol)
    draw.ellipse((5 * k - k // 5, 20 * k - k // 5, 5 * k + k // 5, 20 * k + k // 5), width=lw, outline=lcol)
    draw.line((8 * k, 11 * k, 6 * k, 15 * k), width=lw, fill=lcol)
    draw.line((6 * k, 15 * k, 5 * k, 20 * k), width=lw, fill=lcol)
    draw.line((5 * k, 20 * k, 7 * k, 20 * k), width=lw, fill=lcol)
    # правая нога
    draw.ellipse((11 * k - k // 5, 10 * k - k // 5, 11 * k + k // 5, 10 * k + k // 5), width=lw, outline=lcol)
    draw.ellipse((13 * k - k // 5, 15 * k - k // 5, 13 * k + k // 5, 15 * k + k // 5), width=lw, outline=lcol)
    draw.line((8 * k, 11 * k, 11 * k, 10 * k), width=lw, fill=lcol)
    draw.line((11 * k, 10 * k, 13 * k, 15 * k), width=lw, fill=lcol)
    draw.line((13 * k, 15 * k, 15 * k, 14 * k), width=lw, fill=lcol)
    im.save('human.png')
