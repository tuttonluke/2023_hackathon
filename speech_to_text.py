import whisper

import pyaudio
import numpy as np
import text_to_morse
import threading


model = whisper.load_model('medium', device='cuda', download_root='.')

chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
frame_rate = 16000

class Streamer():
    def __init__(self) -> None:
        self.frames = []
        self.recording = False


    def start_recording(self):
        self.p = pyaudio.PyAudio()
        self.recording = True
        self.frames = []

        self.stream = self.p.open(
            format=sample_format,
            channels=channels,
            rate=frame_rate,
            input=True,
            output=True,
            frames_per_buffer=chunk
        )

        t = threading.Thread(target=self._record)
        t.start()

    
    def _record(self):
        while self.recording:
            data = self.stream.read(chunk)
            self.frames.append(data)
    
    def play_audio(self):
        audio = np.frombuffer(np.array(self.frames), np.int16).astype(np.float32) * (1 / 32768.0)
        result = model.transcribe(audio)
        text = result['text']
        print(text)
        morse = text_to_morse.translate(text)
        print(morse)
        text_to_morse.morse_beep(morse)


    def stop_recording(self,):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
    