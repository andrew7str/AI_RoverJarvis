import os
from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("model-vosk")  # folder model vosk
rec = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def listen():
    print("🎙️ Mendengarkan...")
    text = ""
    while True:
        data = stream.read(4096)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            if text:
                print(f"🗣️ Kamu: {text}")
                return text
