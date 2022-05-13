# Если на картинке самое главное находится в центре, а остальное пусто или не интересно, то можно вырезать центральную часть и заключить в рамочку.
# Напишите функцию frame(), которая принимает имя файла и ширину рамки, вырезает центральную часть изображения (треть размера по ширине и по высоте, используйте целочисленное деление) и добавляет рамку переданной ширины по контуру, цвет рамки – средний цвет вырезанной центральной части. Затем сохраняет его в файл done.png.
# Для определения среднего цвета нужно найти сумму красной составляющей всех пикселей и поделить нацело на количество пикселей, затем то же сделать для остальных составляющих.
#
# Формат ввода
# Пример вызова функции:
#
# frame("bug.png", 20)
# Для рисунка:
from PIL import Image, ImageOps


def frame(name, ramka):
    im = Image.open(name)
    pixels = im.load()
    x, y = im.size
    im2 = im.crop(((x - x // 3) // 2, (y - y // 3) // 2, (x + x // 3) // 2, (y + y // 3) // 2))
    pixels = im2.load()
    x, y = im2.size
    border_color = (sum([pixels[i, j][0] for j in range(y) for i in range(x)]) // (x * y),
                    sum([pixels[i, j][1] for j in range(y) for i in range(x)]) // (x * y),
                    sum([pixels[i, j][2] for j in range(y) for i in range(x)]) // (x * y))
    img_border = ImageOps.expand(im2, border=ramka, fill=(border_color))
    img_border.save('done.png')