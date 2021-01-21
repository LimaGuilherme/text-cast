from speech_recognition import Recognizer


class Transcribe:

    def __init__(self):
        self.recognizer = Recognizer()

    def to_text(self):
        aaa = self.recognizer.recognize_google(audio_content, language='pt-BR')
