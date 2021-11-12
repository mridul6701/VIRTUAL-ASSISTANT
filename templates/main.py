import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser

listener = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold=10000
            listener.adjust_for_ambient_noise(source,1.2)
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except LookupError:
        print("COULD NOT UNDERSTAND AUDIO")
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:
        search=command.replace('search','')
        talk('searching'+ search)
        pywhatkit.search(search)

    elif 'date' in command:
        date = datetime.date.today()
        print(date)
        talk('CURRENT DATE IS ' + str(date))

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('CURRENT TIME IS ' + time)

    elif 'are you single' in command:
        talk('I AM IN RELATIONSHIP WITH YOU')

    elif 'hello' in command:
        talk('HELLO, HOW MAY I HELP YOU')

    elif 'owner' in command:
        talk('MRIDUL ANAND')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'instagram' in command:
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        talk("opening instagram")

    elif 'facebook' in command:
        url = "https://Facebook.com/"
        webbrowser.get().open(url)
        talk("opening Facebook")

    elif 'mail' in command:
        url = "https://mail.google.com/mail/u/0/"
        webbrowser.get().open(url)
        talk("opening Mail")

    elif 'twitter' in command:
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        talk("opening twitter")

    elif 'prime minister' in command:
        talk('MR.NARINDER MODI')

    elif 'amazon' in command:
        url = "https://www.amazon.in"
        webbrowser.get().open(url)
        talk("opening amazon")

    elif 'weather' in command:
        url = "https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN945IN945&oq=whea&aqs=chrome.1.69i57j0i10i131i433j46i67j0i67j46i67j0i10i433j46i67l3j0i10i131i433.3456j1j7&sourceid=chrome&ie=UTF-8/"
        webbrowser.get().open(url)
        talk("Here is what I found for on google")
    else:
        talk('Please say the command again')
run_alexa()