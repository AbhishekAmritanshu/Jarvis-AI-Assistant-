import pyttsx3
import datetime
import wikipedia
import SpeechRecognition as SR

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print voice
#print(voices[0].id)
engine = setProperty('voice', voices[0].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
  def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("Good morning")

    elif hour>=12 and hour<18:
      speak("Good afternoon")

    else:
        speak("Good evening")
        speak("I am Jarvis Sir, please tell me how I may help you")

  def takeCommand():
    #take input from microphone and start giving output
    r= SR.recognizer()
    with SR.microphone as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)

  try:
    print("recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said: {query}\n")
  
  except Exception as e:
    print(e)

    print("say that again please...")
    return "None"
  return query


  if __name__== "__main__":

    wishMe()
    while True:
     query = takeCommand().lower()
  if 'wikipedia' in Query:
    speak('searching wekipedia...', "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)



