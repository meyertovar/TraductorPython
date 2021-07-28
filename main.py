from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageTk
import pytesseract
from googletrans import Translator
import cv2
import imutils
import numpy as np

try:
    from PIL import Image
except ImportError:
    import Image


# function to choose the language to translate the image
def english_idiom():
    global image

    if selected.get() == 1:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img_text = pytesseract.image_to_string(image)

        p = Translator()
        p_translated = p.translate(img_text, dest='spanish')
        translated = str(p_translated.text)

        imas = Image.open("pictures/plantillaTradu.png")
        draw = ImageDraw.Draw(imas)
        font = ImageFont.truetype(r'C:\fonts\Roboto-Black.ttf', 18)
        text = translated
        draw.text((15, 20), text, fill="black", font=font, align="right")

        imas.save("test.png")
        src = cv2.imread("test.png")
        imageToShowOutput = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShowOutput)
        img = ImageTk.PhotoImage(image=im)
        lblOutputImage.configure(image=img)
        lblOutputImage.image = img

        # Label IMAGEN DE SALIDA
        lblInfo3 = Label(root, text="IMAGEN DE SALIDA:")
        lblInfo3.grid(column=1, row=0, padx=5, pady=5)


def selected_image():
    path_image = filedialog.askopenfilename(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])

    if len(path_image) > 0:
        global image

        image = cv2.imread(path_image)
        image = imutils.resize(image, height=520)

        imageToShow = imutils.resize(image, width=540)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        # Label imagen a traducir
        lblInfo1 = Label(root, text="Imagen a traducir:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

        lblOutputImage.image = ""
        selected.set(0)


image = None

# modal principal
root = Tk()
# root.geometry("200x200")
root.title("Traductor de Imagenes")

lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Label donde se presentará la imagen de salida
lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=1, rowspan=6)

lblInfo2 = Label(root, text="Escoge el idioma para traducir", width=25)
lblInfo2.grid(column=0, row=3, padx=5, pady=5)

selected = IntVar()
radio1 = Radiobutton(root, text="Ingles", width=25, value=1, variable=selected, command=english_idiom)
radio2 = Radiobutton(root, text="Aleman", width=25, value=2, variable=selected, command=english_idiom)
radio1.grid(column=0, row=4)
radio2.grid(column=0, row=5)

btn = Button(root, text="Seleccionar imagen", width=25, command=selected_image)
btn.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()
