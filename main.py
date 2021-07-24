import pytesseract
from googletrans import Translator

try:
    from PIL import Image
except ImportError:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ima = Image.open("Captura.JPG")
img_text = pytesseract.image_to_string(ima)
print(img_text)

p = Translator()
p_translated = p.translate(img_text, dest='spanish')
translated = str(p_translated.text)
print(translated)

with open('traduccion.txt', mode='w') as file:
    file.write(img_text + "\n\n\n" + translated)
    print("hecho!")
