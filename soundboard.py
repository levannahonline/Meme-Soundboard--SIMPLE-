import tkinter as tk
import pygame
import os
from functools import partial

pygame.mixer.init(frequency=44100, channels=32, buffer=512)

class SoundPlayer:
    def __init__(self):
        self.sounds = {} 
        
    def load_sounds(self, sound_dict):
        
        for name, path in sound_dict.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(path)
            except Exception as e:
                print(f"Failed to load {name}: {e}")
                self.sounds[name] = None

    def play(self, name):
        if name in self.sounds and self.sounds[name]:
            pygame.mixer.stop()  # Stop all currently playing sounds
            channel = pygame.mixer.find_channel()
        if channel:
            channel.play(self.sounds[name])

def main():
    root = tk.Tk()
    root.title("Reliable Soundboard")
    root.geometry("500x700")
    
    player = SoundPlayer()

    sound_dict = {
        "arab meme": "sounds/arabic-ah.wav",
        "dang shawty": "sounds/dang-shawty.wav",
        "ewww": "sounds/ewww-get-off.wav",
        "grr": "sounds/fantomel-ft-kate-linn-dame-un-grrr.wav",
        "flashbang": "sounds/flashbang.wav",
        "gta": "sounds/gta-san-andreas-cj-burning.wav",
        "ight bet": "sounds/ight-bet.wav",
        "microsoft scammer": "sounds/indian-scammer.wav",
        "gay": "sounds/gay.wav",
        "laughing": "sounds/laugh-tracks.wav",
        "lebron": "sounds/lebron-bo-bo-boom.wav",
        "cheese": "sounds/sometimes-i-dream-about-cheese.wav",
        " wah": "sounds/ wah-wah-wah.wav",
        "a boy": "sounds/you're-a-boy-in-a-man's-world.wav",

    }
    
    for path in sound_dict.values():
        if not os.path.exists(path):
            print(f"Missing file: {path}")
    
    player.load_sounds(sound_dict)

    for text in sound_dict:
        btn = tk.Button(
            root,
            text=text,
            command=partial(player.play, text),
            bg="#3243C4",
            fg="#C1C6F3",
            font=("Helvetica", 12, "bold"),
            height=2,
            width=25
        )
        btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()