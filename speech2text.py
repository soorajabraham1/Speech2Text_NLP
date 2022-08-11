import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()

r2=sr.Recognizer()
r3=sr.Recognizer()


with sr.Microphone(device_index=0) as source:
    print('[search Sooraj: search youtube]')
    print('speak now')
    audio=r3.listen(source)
    print(r2.recognize_google(audio))
if 'Wikipedia' in r2.recognize_google(audio):
    r2= sr.Recognizer()
    url='https://en.wikipedia.org/wiki/'
    
    with sr.Microphone() as source:
        print('search')
        audio=r2.listen(source)
        try:
            get= r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)

        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))