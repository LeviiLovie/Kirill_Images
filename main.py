from PIL import Image
from PIL import ImageFilter
# Переменные смен цвета
pixel = (0, 0, 0)
pixelRight = (0, 0, 0)
cmena = False
pR = 0
pG = 0
pb = 0

# Открытие изображениия и применениие фильтров
image_name = input("Print image name: ")
image = Image.open(image_name)
image = image.filter(ImageFilter.SHARPEN)

# Запрашиваю параметры парогов смены цвета
pR = int(input("Parogue for red channel: "))
pG = int(input("Parogue for green channel: "))
pB = int(input("Parogue for blue channel: "))

# Вывод параметров изображения и парогов восприятия
print("Image: ", image.format, image.size, image.mode)
print("Parogue (RGB): ", pR, pG, pB)

# Работаю с изображением
print("Working with image")
for i in range(0, image.size[0]):
    for j in range(0, image.size[1]):
        # Пиксели цвета (0, 0, 0) крашу в (1, 1, 1)
        if image.getpixel((i, j)) == (0, 0, 0): image.putpixel((i, j), (1, 1, 1))
        
        # Крашу линии
        pixel = image.getpixel((i, j))
        if j < image.size[1] - 1:
            pixelRight = image.getpixel((i, j + 1))
        
        if abs(pixel[0] - pixelRight[0]) > pR: cmena = True
        if abs(pixel[1] - pixelRight[1]) > pG: cmena = True
        if abs(pixel[2] - pixelRight[2]) > pB: cmena = True

        if cmena == True:
            image.putpixel((i, j), (0, 0, 0))
            cmena = False

        # Пиксели цвета > (0, 0, 0) крашу в (255, 255, 255)
        if image.getpixel((i, j)) > (0, 0, 0): image.putpixel((i, j), (255, 255, 255))

# Сохранение и показ изображения
image.save("result5.png")
image.show()