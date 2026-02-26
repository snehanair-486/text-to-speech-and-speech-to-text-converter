# Text-to-Speech and Speech-to-Text Converter

A simple Python app to convert Text to Speech and Speech to Text.

## Features
- 🔊 **Text → Speech (TTS):** Converts any typed text into spoken audio using the `pyttsx3` library, which works completely offline using your system's built-in voice engine.
- 🎤 **Speech → Text (STT):** Captures audio from your microphone and converts it into text using the `SpeechRecognition` library, which sends the audio to Google's Speech API to process and return the result.
- 🔄 **Speak it back:** A combined mode where you speak into the microphone, your speech is converted to text, and then that text is immediately read back to you out loud.

## Requirements
- Python 3.x
- Internet connection (for Speech to Text)

## Setup
pip install -r requirements.txt

## Run
python main.py
