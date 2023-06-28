#%%
import os
import json
import winsound
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

def get_list_of_json_files():
    for root, dirs, files in os.walk(json_files_folder):
        return files

def read_json_file(path):
    with open(path, "r") as json_data:
        text_dict = json.load(json_data)
        return text_dict["text"]

def translate(text):
    return " ".join(LETTERS_TO_MC[char] for char in text.upper())

def morse_beep(morse_string):
    for char in morse_string:
        if char == ".":
            winsound.Beep(440, 100)
        elif char == "-":    
            winsound.Beep(440, 300)
        else:
            continue
#%%
if __name__ == "__main__":
    for file in get_list_of_json_files():
        text = read_json_file(f"{json_files_folder}/{file}")
        morse_text = translate(text)
        morse_beep(morse_text)


    



        