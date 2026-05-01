import pygame
import customtkinter as tk
from customtkinter import CTkImage
from PIL import Image
import time
from pathlib import Path
root = tk.CTk()
root.title("Music Player")
root.geometry("500x500")
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
mus=pygame.mixer.music.load("R1B.ogg")
pygame.mixer.music.play()
from tinytag import TinyTag

file_path = "R1B.ogg"
filename = Path(file_path).stem
print(filename)
tag = TinyTag.get('R1B.ogg')
songtit=tag.title
songartist=tag.artist
album=tag.album
#img=tag.get_image()
#if img:
    #with open('cover_art.jpg', 'wb') as f:
        #f.write(img)
songname = tk.CTkLabel(root, text=songtit, font=("Arial", 22))
songname.place(relx=0.5, rely=0.1, anchor='c')
songart = tk.CTkLabel(root, text=songartist, font=("Arial", 15))
songart.place(relx=0.5, rely=0.15, anchor='c')
songal = tk.CTkLabel(root, text=album, font=("Arial", 15))
songal.place(relx=0.5, rely=0.2, anchor='c')
#my_image = tk.CTkImage(light_image=img,
                         #dark_image=img,
                         #size=(30, 30))
#button = tk.CTkButton(root, text="Click Me", image=my_image)
#button.pack(pady=20, padx=20)
root.mainloop()
time.sleep(50)
