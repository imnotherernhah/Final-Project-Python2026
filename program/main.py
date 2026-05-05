import math
import pygame
import io
import customtkinter as tk
from customtkinter import CTkImage, CTkCanvas
from tkinter import filedialog
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
pathtosng=""
name=""
State=0

def OpenFile():
    global pathtosng
    pathtosng = filedialog.askopenfilename(
        initialdir="/",
        title="Choose an audio file to play.",
        filetypes=(("Supported audio files (.ogg, .wav, .mp3, .flac)", "*.ogg; *.wav; *.mp3; *.flac"),
                   ("All files", "*.*"))
    )
    global name
    pat = Path(pathtosng)
    name = pat.name
    mus = pygame.mixer.music.load(pathtosng)
    pygame.mixer.music.play()
    MainProg()

def ClrSong():
    songname = tk.CTkLabel(root, text="No Song", font=("Arial", 20))
    songname.place(relx=0.5, rely=0.665, anchor='c')
    songart = tk.CTkLabel(root, text="No Artist", font=("Arial", 15))
    songart.place(relx=0.5, rely=0.715, anchor='c')
    songal = tk.CTkLabel(root, text="No Album", font=("Arial", 17))
    songal.place(relx=0.5, rely=0.76, anchor='c')
    cover = tk.CTkImage(light_image=Image.open("fail.png"), dark_image=Image.open("fail.png"), size=(300, 300))
    label = tk.CTkLabel(root, image=cover, text="")
    label.place(relx=0.5, rely=0.34, anchor='c')
    button = tk.CTkButton(root, text="", width=30)
    button.place(relx=0.5, rely=0.85, anchor='c')
    button2 = tk.CTkButton(root, text="📁", width=30)
    button2.place(relx=0.4, rely=0.85, anchor='c')
def updProgBar(progbar,tag, elapsed, tota):
    tottime=tag.duration
    #print(round(tottime/60,2))
    secs=(pygame.mixer_music.get_pos())/1000
    progbar.set(secs/tottime)
    elapsed.configure(text=timedelta(seconds=math.trunc(secs)))
    tota.configure(text=timedelta(seconds=math.trunc(tottime)))
    root.update()
def Pause():
    pygame.mixer.music.pause()
    global State
    State=1
    global button
    DisplayGUIButton(button)

def Play():
    pygame.mixer.music.unpause()
    global State
    State=0
    global button
    DisplayGUIButton(button)

def DisplayGUIButton(button):
    if State==0:
        button.configure(text="⏸", command=Pause)
    if State==1:
        button.configure(text="▶︎", command=Play)

def MainProg2():
    tag = TinyTag.get(pathtosng, image=True)
    if tag.title is None:
        songtit=name
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
    songname.configure(text=songtit)
    songart.configure(text=songartist)
    songal.configure(text=album)
    cover = tk.CTkImage(light_image=Image.open("cover.png"), dark_image=Image.open("cover.png"), size=(300, 300))
    label = tk.CTkLabel(root, image=cover, text="")
    label.place(relx=0.5, rely=0.34, anchor='c')
    progressbar = tk.CTkProgressBar(root, orientation="horizontal",progress_color="purple")
    progressbar.place(relx=0.5, rely=0.81, anchor='c')
    elap = tk.CTkLabel(root, text="", font=("Arial", 17))
    elap.place(relx=0.17, rely=0.81, anchor='w')
    tot = tk.CTkLabel(root, text="", font=("Arial", 17))
    tot.place(relx=0.71, rely=0.81, anchor='w')
    button2.configure(command=OpenFile)
    global button
    DisplayGUIButton(button)
    while True:
        updProgBar(progressbar, tag, elap,tot)

def MainProg():
    root.update()
    if pathtosng == "":
        OpenFile()
    file_path = pathtosng
    filename = Path(file_path).stem
    print(filename)
    tag = TinyTag.get(pathtosng, image=True)
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
songname = tk.CTkLabel(root, text="No Song", font=("Arial", 20))
songname.place(relx=0.5, rely=0.665, anchor='c')
songart = tk.CTkLabel(root, text="No Artist", font=("Arial", 15))
songart.place(relx=0.5, rely=0.715, anchor='c')
songal = tk.CTkLabel(root, text="No Album", font=("Arial", 17))
songal.place(relx=0.5, rely=0.76, anchor='c')
cover = tk.CTkImage(light_image=Image.open("fail.png"), dark_image=Image.open("fail.png"), size=(300, 300))
label = tk.CTkLabel(root, image=cover, text="")
label.place(relx=0.5, rely=0.34, anchor='c')
button = tk.CTkButton(root, text="⏸", width=30)
button.place(relx=0.5, rely=0.85, anchor='c')
button2 = tk.CTkButton(root, text="📁", width=30)
button2.place(relx=0.4, rely=0.85, anchor='c')
#print(f"Selected file: {pathtosng}")
MainProg()
#root.mainloop()