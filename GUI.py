from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import os

# Переменная экрана и параметры экрана
root = Tk()
root.title("Coloring utility")
root.geometry("450x375")
root.resizable(width = False, height = False)

# Переменные для обработки изобрадениия
pixel = (0, 0, 0)
pixelRight = (0, 0, 0)
pR = 0
pG = 0
pB = 0

# Функции
def openfile():
    filepath = filedialog.askopenfile(title="Select file")
    print(filepath.read())
def get_value(entryWidget):
    value = entryWidget.get()
    try:
        return int(value)
    except ValueError:
        return None
def result():
    print("Working")
    upfilename = Image.open(downfilenames[0])
    for i in range(0, upfilename.size[0]):
        for j in range(0, upfilename.size[1]):
            # Пиксели цвета (0, 0, 0) крашу в (1, 1, 1)
            if upfilename.getpixel((i, j)) == (0, 0, 0): upfilename.putpixel((i, j), (1, 1, 1))
    for i in range(0, upfilename.size[0]):
        for j in range(0, upfilename.size[1]):
            cmena = False
            
            # Крашу линии
            pixel = upfilename.getpixel((i, j))
            if j < upfilename.size[1] - 1:
                pixelRight = upfilename.getpixel((i, j + 1))
            
            if abs(pixel[0] - pixelRight[0]) > get_value(pR): cmena = True
            if abs(pixel[1] - pixelRight[1]) > get_value(pG): cmena = True
            if abs(pixel[2] - pixelRight[2]) > get_value(pB): cmena = True

            if cmena == True:
                upfilename.putpixel((i, j), (0, 0, 0))
                cmena = False
    for i in range(0, upfilename.size[0]):
        for j in range(0, upfilename.size[1]):
            # Пиксели цвета > (0, 0, 0) крашу в (255, 255, 255)
            if upfilename.getpixel((i, j)) > (0, 0, 0): upfilename.putpixel((i, j), (255, 255, 255))
    for i in range(0, upfilename.size[0]):
        for j in range(0, upfilename.size[1]):
            kolvo = 0
            if upfilename.getpixel((i, j)) == (0, 0, 0):
                if i > 0 and upfilename.getpixel((i - 1, j)) == (255, 255, 255): kolvo += 1
                if i < upfilename.size[0] - 1 and upfilename.getpixel((i + 1, j)) == (255, 255, 255): kolvo += 1
                if j > 0 and upfilename.getpixel((i, j - 1)) == (255, 255, 255): kolvo += 1
                if j < upfilename.size[1] - 1 and upfilename.getpixel((i, j + 1)) == (255, 255, 255): kolvo += 1
            if kolvo < 1:
                upfilename.putpixel((i, j), (255, 255, 255))
    upfilename.show()

# Получение и обработка путя к файлу
filetypes = (
    ('IMG files', '*.jpg ' + '*,jpeg ' + '*.png '),
    # ('IMG files', '*.jpg'),
    ('All files', '*.*')
)
downfilenames = fd.askopenfilenames(
    title='Coloring utility/open file',
    initialdir='/',
    filetypes=filetypes)
upfilenames = Image.new(mode = "RGB", size = (1, 1))
curDir = os.getcwd()
fn = curDir
downIMG = ImageTk.PhotoImage(Image.open(downfilenames[0]).resize((320, 240)))
downIMGLable = Label(image = downIMG)
upIMG = ImageTk.PhotoImage(Image.open(downfilenames[0]).resize((320, 240)))
upIMGLable = Label(image = upIMG)
upIMGLable.grid(row = 6, column = 2)

# СОздание элементов экрана
pR = Entry(text = "Red porogue")
pG = Entry(text = "Green porogue")
pB = Entry(text = "blue porogue")
pRtext = Label(text = "Red porogue:")
pGtext = Label(text = "Green porogue:")
pBtext = Label(text = "blue porogue:")
result = Button(text = "Result", command = result)

#  Размешение элементов на экраме при помощи grid
pR.grid(row = 1, column = 2)
pG.grid(row = 2, column = 2)
pB.grid(row = 3, column = 2)
pRtext.grid(row = 1, column = 1)
pGtext.grid(row = 2, column = 1)
pBtext.grid(row = 3, column = 1)
result.grid(row = 5, column = 2)

# Бесконечный цикл обработки экрана
root.mainloop()