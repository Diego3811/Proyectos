import speech_recognition as sr
import pyttsx3

class AIAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
        # Configurar voz en español
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "spanish" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)

    def process_audio(self, audio_data):
        # Aquí irá la lógica de procesamiento
        try:
            text = self.recognizer.recognize_google(audio_data, language="es-ES")
            return self.generate_response(text)
        except:
            return "No pude entender el audio"

    def generate_response(self, text):
        if "hola" in text.lower():
            return "¡Hola! Soy NOVA, tu asistente virtual. ¿En qué puedo ayudarte?"
        elif "nombre" in text.lower():
            return "Mi nombre es NOVA, que significa Neural Operative Virtual Assistant"
        elif "qué eres" in text.lower():
            return "Soy NOVA, una inteligencia artificial diseñada para ayudarte"
        # Añade más respuestas aquí
        return f"Procesando: {text}"
