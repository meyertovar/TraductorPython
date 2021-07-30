from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageTk
import pytesseract
from googletrans import Translator
import cv2
import imutils

try:
    from PIL import Image
except ImportError:
    import Image


# function to choose the language to translate the image
def english_idiom():
    global image, img_text

    if selected.get() == 1:
        # tesseract must be installed in windows and indicate the path so that it does not generate errors
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img_text = pytesseract.image_to_string(image)
        # Image converted to text and translated into Spanish
        p = Translator()
        p_translated = p.translate(img_text, dest='spanish')
        translated = str(p_translated.text)
        # translated text font type settings, and on which image we will send the text.
        imas = Image.open("pictures/plantillaTraductor.jpg")
        draw = ImageDraw.Draw(imas)
        font = ImageFont.truetype(r'C:\fonts\Roboto-Black.ttf', 18)
        text = translated
        draw.text((15, 20), text, fill="black", font=font, align="right")
        # image with the translated text that we will use late
        imas.save("test.png")
        src = cv2.imread("test.png")
        # we will display the image in the GUI in the lblOutputImage
        imageToShowOutput = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShowOutput)
        img = ImageTk.PhotoImage(image=im)
        lblOutputImage.configure(image=img)
        lblOutputImage.image = img

        # output image label
        lblInfo3 = Label(root, text="IMAGEN DE SALIDA:")
        lblInfo3.grid(column=1, row=0, padx=5, pady=5)

    with open('traduccion.txt', mode='w') as file:
        file.write(img_text + "\n\n\n" + translated)
        print("hecho!")


# function to choose the language
def selected_image():
    # specify file type for images
    path_image = filedialog.askopenfilename(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])
    # if there is a path we declare image globally
    if len(path_image) > 0:
        global image
        # we read the image and resize it
        image = cv2.imread(path_image)
        image = imutils.resize(image, height=340)
        # display image and input in GUI
        imageToShow = imutils.resize(image, width=320)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)
        lblInputImage.configure(image=img)
        lblInputImage.image = img

        # Label image to translate- image entrace
        lblInfo1 = Label(root, text="Imagen a traducir:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)
        # we clean the radio button selection
        lblOutputImage.image = ""
        selected.set(0)


image = None

# modal principal
root = Tk()
root.title("Traductor de Imagenes")
# Label where the input image will be presented
lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

# Label where the output image will be presented
lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=1, rowspan=6)

lblInfo2 = Label(root, text="Escoge el idioma para traducir", width=25)
lblInfo2.grid(column=0, row=3, padx=5, pady=5)
# selected allows us to handle integers for radio button
selected = IntVar()
# radio button where we pass the modal root, and call the function of english_idiom
radio1 = Radiobutton(root, text="Ingles", width=25, value=1, variable=selected, command=english_idiom)
radio2 = Radiobutton(root, text="Aleman", width=25, value=2, variable=selected, command=english_idiom)
radio1.grid(column=0, row=4)
radio2.grid(column=0, row=5)
# button selected input image
btn = Button(root, text="Seleccionar imagen", width=25, command=selected_image)
btn.grid(column=0, row=0, padx=5, pady=5)
# an endless loop is created where we have already declared root, until the user closes the window
root.mainloop()


