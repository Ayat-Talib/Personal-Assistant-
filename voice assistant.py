import pyttsx3  # text to speech
import speech_recognition as sr
import webbrowser
import datetime


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # for noise removal
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"Recognized: {data}")
            return data
        except sr.UnknownValueError:
            print("Didn't get your voice!")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""


def speechtx(text, voice_index=1, rate=150):  # text to speech
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice_index >= len(voices):
        voice_index = 0  # default to the first voice if index is out of range
    engine.setProperty("voice", voices[voice_index].id)
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()


def process_command(command):
    command = command.lower()
    if "your name" in command:
        response = "My name is Ayat"
    elif "how old are you" in command:
        response = "I am one year old"
    elif "time" in command:
        response = datetime.datetime.now().strftime("%I:%M %p")
    elif 'google' in command:
        webbrowser.open_new_tab("https://www.google.com/")
        response = "Opening Google"
    elif "facebook" in command:
        webbrowser.open_new_tab("https://www.facebook.com/")
        response = "Opening Facebook"
    elif "watsapp" in command:
        webbrowser.open_new_tab('https://web.whatsapp.com/')
        response = "Opening watsapp"
    elif "exit the program" in command:
        response = "Thank you"
        return response, True
    else:
        response = "Sorry, I didn't understand that."
    return response, False


def main():
    speechtx("Hello! How can I help you today?")
    while True:
        command = sptext()
        if command:
            response, should_exit = process_command(command)
            speechtx(response)
            if should_exit:
                break
        else:
            speechtx("Please say something.")


if __name__ == '__main__':
    main()
