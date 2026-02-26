import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    
    engine.setProperty('volume', 1.0)  
    print(f"\nSpeaking: {text}")
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=10)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"API error: {e}")
    return None

def main():
    while True:
        print("\n===== TTS / STT Converter =====")
        print("1. Text → Speech")
        print("2. Speech → Text")
        print("3. Speech → Text → Speak it back")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            text = input("Enter text to speak: ")
            text_to_speech(text)

        elif choice == "2":
            speech_to_text()

        elif choice == "3":
            result = speech_to_text()
            if result:
                text_to_speech(result)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()