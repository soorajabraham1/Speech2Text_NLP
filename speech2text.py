import speech_recognition as sr
import webbrowser as wb

r2=sr.Recognizer()
r3=sr.Recognizer()


with sr.Microphone(device_index=0) as source:
    print('speak now')
    audio=r3.listen(source)
    engine=r2.recognize_google(audio)
    print(engine)

url1='https://www.'
url2='.com/search?q='
    
with sr.Microphone() as source:
    print('search')
    audio=r2.listen(source)
    try:
        get= r2.recognize_google(audio)
        print(get)
        wb.get().open_new(url1+engine+url2+get)

    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))