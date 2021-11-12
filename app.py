from flask import Flask, render_template
import jyserver.Flask as jsf
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser

app = Flask(__name__)


@jsf.use(app)
class App:
   def __init__(self):
      self.show="clicked"
   def data(self):
      
      listener = sr.Recognizer()
      engine = pyttsx3.init()
      rate = engine.getProperty('rate')
      engine.setProperty('rate',130)
      voices = engine.getProperty('voices')
      engine.setProperty('voice', voices[1].id)

      def talk(text):
               engine.say(text)
               engine.runAndWait() #yaha dikat hai 
      def take_command():
         try:
            with sr.Microphone() as source:
                  listener.energy_threshold=10000
                  listener.adjust_for_ambient_noise(source,1.2)
                  print('Listening...')
                  self.js.document.getElementById('txtMsg').style.display='block'
                  self.js.document.getElementById('txtMsg').innerHTML='<p>Listening...</p>'
                  voice = listener.listen(source)
                  command = listener.recognize_google(voice)
                  command = command.lower()
                  self.js.document.getElementById('txtMsg').innerHTML='<p>'+command+'</p>'
                  print(command)
         except LookupError:
            print("COULD NOT UNDERSTAND AUDIO")
            self.js.document.getElementById('txtMsg').innerHTML='<p>COULD NOT UNDERSTAND AUDIO</p>'
         return command


      def run_alexa(command): 
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
      run_alexa(take_command())
      # run_alexa("prime minister")
      # setTimeout(run_alexa(take_command()),1000)

@app.route('/',methods=['GET', 'POST'])
def home():
   return App.render(render_template('index.html'))
if __name__ == '__main__':
   app.run()