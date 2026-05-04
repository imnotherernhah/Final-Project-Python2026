import math
import pygame
import io
import customtkinter as tk
from customtkinter import CTkImage
from PIL import Image
import time
from pathlib import Path
from tinytag import TinyTag
from datetime import timedelta
root = tk.CTk()
root.title("Music Player")
root.geometry("500x500")
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
mus=pygame.mixer.music.load("R1B.ogg")
pygame.mixer.music.play()
def updProgBar(progbar,tag, elapsed, tota):
    tottime=tag.duration
    #print(round(tottime/60,2))
    secs=(pygame.mixer_music.get_pos())/1000
    progbar.set(secs/tottime)
    elapsed.configure(text=timedelta(seconds=math.trunc(secs)))
    tota.configure(text=timedelta(minutes=round(tottime)))
    root.update()

def MainProg2():
    tag = TinyTag.get('R1B.ogg', image=True)
    if tag.title is None:
        songtit=tag.filename
    else:
        songtit=tag.title
    if tag.artist is None:
        songartist="Unknown Artist"
    else:
        songartist=tag.artist
    if tag.album is None:
        album="Unknown Album"
    else:
        album=tag.album
    songname = tk.CTkLabel(root, text=songtit, font=("Arial", 22))
    songname.place(relx=0.5, rely=0.65, anchor='c')
    songart = tk.CTkLabel(root, text=songartist, font=("Arial", 15))
    songart.place(relx=0.5, rely=0.7, anchor='c')
    songal = tk.CTkLabel(root, text=album, font=("Arial", 20))
    songal.place(relx=0.5, rely=0.75, anchor='c')
    cover = tk.CTkImage(light_image=Image.open("cover.png"), dark_image=Image.open("cover.png"), size=(300, 300))
    label = tk.CTkLabel(root, image=cover, text="")
    label.place(relx=0.5, rely=0.3, anchor='c')
    progressbar = tk.CTkProgressBar(root, orientation="horizontal",progress_color="purple")
    progressbar.place(relx=0.5, rely=0.81, anchor='c')
    elap = tk.CTkLabel(root, text="", font=("Arial", 17))
    elap.place(relx=0.17, rely=0.81, anchor='w')
    tot = tk.CTkLabel(root, text="", font=("Arial", 17))
    tot.place(relx=0.71, rely=0.81, anchor='w')
    while True:
        updProgBar(progressbar, tag, elap,tot)

def MainProg():
    file_path = "R1B.ogg"
    filename = Path(file_path).stem
    print(filename)
    tag = TinyTag.get('R1B.ogg', image=True)
    songtit=tag.title
    songartist=tag.artist
    album=tag.album
    if tag.images.front_cover is None:
        img=Image.open("fail.png")
        img.save('cover.png')
    else:
        img=tag.images.front_cover
        imgdat=img.data
        img2 = Image.open(io.BytesIO(imgdat))
        img2.save('cover.png')
    MainProg2()

MainProg()
#root.mainloop()