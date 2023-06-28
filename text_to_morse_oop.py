#%%
import os
import json
import winsound
import time
import string
#%%
class TextToMorse:
    def __init__(self) -> None:
        self.LETTERS_TO_MC = {
                                    'A': '.-', 'B': '-...', 'C': '-.-.',
                                    'D': '-..', 'E': '.', 'F': '..-.',
                                    'G': '--.', 'H': '....', 'I': '..',
                                    'J': '.---', 'K': '-.-', 'L': '.-..',
                                    'M': '--', 'N': '-.', 'O': '---',
                                    'P': '.--.', 'Q': '--.-', 'R': '.-.',
                                    'S': '...', 'T': '-', 'U': '..-',
                                    'V': '...-', 'W': '.--', 'X': '-..-',
                                    'Y': '-.--', 'Z': '--..',  '1': '.----',
                                    '2': '..---', '3': '...--', '4': '....-',
                                    '5': '.....', '6': '-....', '7': '--...',
                                    '8': '---..', '9': '----.', '0': '-----',
                                    ' ': '/'
                                }
        self.json_files_folder = "json_files"
        self.beep_frequency = 440 # Hz
        self.dot_beep_duration = 100 # miliseconds
        self.dash_beep_duration = 300 # miliseconds
        self.space_beep_duration = 700 # miliseconds
    
    def get_list_of_json_files(self):
        for root, dirs, files in os.walk(self.json_files_folder):
            return files
        
    def read_json_file(self, path):
        with open(path, "r") as json_data:
            text_dict = json.load(json_data)
            return text_dict["text"]

    def translate(self, text):
        remove_punctuation = text.translate(str.maketrans('', '', string.punctuation))
        return " ".join(self.LETTERS_TO_MC[char] for char in remove_punctuation.upper())
    
    def morse_beep(self, morse_string):
        for char in morse_string:
            if char == ".":
                winsound.Beep(self.beep_frequency, self.dot_beep_duration)
            elif char == "-":    
                winsound.Beep(self.beep_frequency, self.dash_beep_duration)
            elif char == "/":
                time.sleep(0.7)
            else:
                continue

#%%
if __name__ == "__main__":
    beeper = TextToMorse()
    file = beeper.get_list_of_json_files()[0]
    text = beeper.read_json_file(f"{beeper.json_files_folder}/{file}")
    beeper.morse_beep(beeper.translate(text))