import speech_recognition as sr
import webbrowser as wb

# creamos una instancia de la clase Recognizer
r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

# usamos la clase Microphone para capturar el audio
with sr.Microphone() as source:
    print('Por favor di algo : ')
    # el audio sera capturado con el metodo lsiten
    audio = r2.listen(source)
    try:
        # usamos Recognizer de google para convertir el audio en texto
        text = r2.recognize_google(audio, language='es-ES')
        print('Acabas de decir: {}'.format(text))
    except sr.UnknownValueError:
        print('Disculpa no te escucho')
    except sr.RequestError as e:
        print("Fallo".format(e))

# creamos una condicion par abrir una url en el navegador usando dos palabras
if "community" in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.python.org/'
    with sr.Microphone() as source:
        print('search')
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("Fallo".format(e))

if "navigate" in r.recognize_google(audio):
    r = sr.Recognizer()
    url = 'https://www.python.org/'
    with sr.Microphone() as source:
        print('search')
        audio = r.listen(source)

        try:
            get = r.recognize_google(audio)
            print(get)
            wb.get().open_new(url)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print("Fallo".format(e))
