#%%
import os
import json
import winsound
import time
import string
#%%
LETTERS_TO_MC = {
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

json_files_folder = "json_files"

beep_frequency = 440 # Hz
unit = 200
dot_beep_duration = 1*unit # miliseconds
dash_beep_duration = 3*unit # miliseconds
intra_char_gap = 1*unit
inter_char_gap = 3*unit
inter_word_gap = 7*unit # miliseconds

def get_list_of_json_files():
    for root, dirs, files in os.walk(json_files_folder):
        return files

def read_json_file(path):
    with open(path, "r") as json_data:
        text_dict = json.load(json_data)
        return text_dict["text"]

def translate(text):
    remove_punctuation = text.translate(str.maketrans('', '', string.punctuation))
    return " ".join(LETTERS_TO_MC[char] for char in remove_punctuation.upper())
 
def morse_beep(morse_string):
    for char in morse_string:
        print(char)
        if char == ".":
            winsound.Beep(beep_frequency, dot_beep_duration)
            time.sleep(intra_char_gap / 1000)
        elif char == "-":    
            winsound.Beep(beep_frequency, dash_beep_duration)
            time.sleep(intra_char_gap / 1000)
        elif char == "/":
            time.sleep((inter_word_gap - (2*inter_char_gap)) / 1000)
        elif char == ' ':
            time.sleep(inter_char_gap/1000)
        else:
            continue
#%%
if __name__ == "__main__":
    for file in get_list_of_json_files():
        text = read_json_file(f"{json_files_folder}/{file}")
        morse_beep(translate(text))




        