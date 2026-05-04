import pygame
import threading
import io
import customtkinter as tk
from customtkinter import CTkImage
from PIL import Image
import time
from pathlib import Path
from tinytag import TinyTag
root = tk.CTk()
root.title("Music Player")
root.geometry("500x500")
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
mus=pygame.mixer.music.load("R1B.ogg")
pygame.mixer.music.play()
def updProgBar(progbar,tag):
    tottime=tag.duration
    #print(round(tottime/60,2))
    secs=(pygame.mixer_music.get_pos())/1000
    progbar.set(secs/tottime)
    root.update()

def MainProg2():
    tag = TinyTag.get('R1B.ogg', image=True)
    songtit=tag.title
    songartist=tag.artist
    album=tag.album
    songname = tk.CTkLabel(root, text=songtit, font=("Arial", 22))
    songname.place(relx=0.5, rely=0.03, anchor='c')
    songart = tk.CTkLabel(root, text=songartist, font=("Arial", 15))
    songart.place(relx=0.5, rely=0.08, anchor='c')
    songal = tk.CTkLabel(root, text=album, font=("Arial", 20))
    songal.place(relx=0.5, rely=0.12, anchor='c')
    cover = tk.CTkImage(light_image=Image.open("cover.png"), dark_image=Image.open("cover.png"), size=(300, 300))
    label = tk.CTkLabel(root, image=cover, text="")  # text="" hides text
    label.place(relx=0.5, rely=0.46, anchor='c')
    progressbar = tk.CTkProgressBar(root, orientation="horizontal")
    progressbar.place(relx=0.5, rely=0.8, anchor='c')
    while True:
        updProgBar(progressbar, tag)

def MainProg():
    file_path = "R1B.ogg"
    filename = Path(file_path).stem
    print(filename)
    tag = TinyTag.get('R1B.ogg', image=True)
    songtit=tag.title
    songartist=tag.artist
    album=tag.album
    img=tag.images.front_cover
    imgdat=img.data
    img2 = Image.open(io.BytesIO(imgdat))
    img2.save('cover.png')
    MainProg2()

MainProg()
#root.mainloop()