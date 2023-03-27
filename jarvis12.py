import pyttsx3 # pyttsx3 for text-to-speech (TTS)
import speech_recognition as sr # speech_recognition for speech-to-text (STT)
import datetime # datetime to get the current time
import wikipedia # wikipedia to search on Wikipedia
import webbrowser # webbrowser to open web browsers to specific websites
import os # os to play music and open files/applications
import smtplib # smtplib to send emails
import requests # requests to get the current weather


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("As slam Aleikum Ustaz!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Janab!")   

    else:
        speak("Good Evening Janab!")  

    speak("I am HABIBI. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('elvispilani@gmail.com', 'Popatlal@786')
    server.sendmail('elvispilani@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")   

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com") 

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")     

        elif 'open the way of tears' in query:
            webbrowser.open("youtube.com/watch?v=YiSQ_db-Dcw")          


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\elvis\\OneDrive\\Desktop\\Visual Studio Code"
            os.startfile(codePath)

        elif 'open quote' in query:
            quote = "C:\\Users\\elvis\\OneDrive\\Desktop\\Quotation.webp"
            os.startfile(quote)


        elif 'email to Arhaan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "elvispilani@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Arhaan. I am not able to send this email")   


        elif 'current weather in' in query:
             reg_ex = speak('current weather in (.*)', query)
        if reg_ex:
              city = reg_ex.group(1)
              weather = weather()
              print(weather)
              location = weather.lookup_by_location(city)
              condition = location.condition()
              speak('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))        

        elif 'how are you' in query:
             speak('I am fine Sir, Thanks For Asking')    

        elif 'pagal hai kya' in query:
             speak('get Lost Idiot') 

        elif 'i want to marry someone' in query:
             speak('Then what are you waiting for idiot. I am a bot and why are you telling me all this stuf')          
               
        elif 'who made you' in query:
             speak('Arhaan Khan, Sir')      

        elif 'crack a joke' in query:
              res = requests.get('https://icanhazdadjoke.com/',
                  headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
             speak(str(res.json()['joke']))
        else:
             speak('oops!I ran out of jokes')







