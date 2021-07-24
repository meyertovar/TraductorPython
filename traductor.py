
import PySimpleGUI as sg
import googletrans
from googletrans import Translator
import threading
import webbrowser
translator = Translator()

class traductor:
    def __init__(self):
        self.datos_lenguajes = googletrans.LANGUAGES
        self.frame_de = [
            [sg.Multiline(default_text='', size=(40, 20), key='-txt_a_traducir_')]
        ]
        frame_a = [
            [sg.Multiline(disabled=True, size=(40, 20), key='-txt_traduccion_')]
        ]
        lenguajesA = ['Detectar idioma']
        lenguajesB = []
        for lenguaje in self.datos_lenguajes.values():
            lenguajesA.append(lenguaje)
            lenguajesB.append(lenguaje)
        # lenguajes= self.lenguajes.keys()
        # print(lenguajes)
        frame_lenguajes = [
            [sg.Text('De')],
            [sg.Combo(values=lenguajesA, key='-lenguaje_de-', default_value='Detectar idioma')],
            [sg.Text('A')],
            [sg.Combo(values=lenguajesB, key='-lenguaje_a-', default_value='english')],
            [sg.Button('Traducir', key='-traducir-')]
        ]

        self.layout_traductor = [[sg.Text('Traductor')],
                                 [sg.Frame('Texto a traducir', self.frame_de, ), sg.Frame('Lenguajes', frame_lenguajes),
                                  sg.Frame('Texto Traducido', frame_a)],

                                 ]


        self.estado_traduccion = False
        self.texto_traduccion = ''