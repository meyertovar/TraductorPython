from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy


def selected_image():
    path_image = filedialog.askopenfilename(filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")])

    if len(path_image) > 0:
        global image

        image = cv2.imread(path_image)
        image = imutils.resize(image, height=550)

        imageToShow = imutils.resize(image, width=790)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        # Label imagen a traducir
        lblInfo1 = Label(root, text="Imagen a traducir:")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

       # lblOutputImage.image = ""
       # selected.set(0)


image = None

# modal principal
root = Tk()

lblInputImage = Label(root)
lblInputImage.grid(column=0, row=2)

lblOutputImage = Label(root)
lblOutputImage.grid(column=1, row=1, rowspan=6)

btn = Button(root, text="Seleccionar imagen", width=25, command=selected_image)
btn.grid(column=0, row=0, padx=5, pady=5)

root.mainloop()
