import math
import pygame
import io
import customtkinter as tk
from customtkinter import CTkImage, CTkCanvas, CTkSlider
from tkinter import filedialog
from PIL import Image
import time
from pathlib import Path
from tinytag import TinyTag
from datetime import timedelta
from pyvidplayer2 import Video
import os
import ffmpeg

root = tk.CTk()
root.title("Music Player")
root.geometry("500x500")
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pathtosng=""
pathtoqsng=""
name=""
State=0
inQueue=0
queue=[]
mode=0

def ChkSongOver():
    for event in pygame.event.get():
        if event.type == isEnd:
            if inQueue==1:
                MainProg()

def OpenFile():
    global pathtosng
    pathtosng = filedialog.askopenfilename(
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
def OpenFile2():
    global pathtoqsng
    pathtoqsng = filedialog.askopenfilename(
        title="Choose an audio file to add to the queue.",
        filetypes=(("Supported audio files (.ogg, .wav, .mp3, .flac)", "*.ogg; *.wav; *.mp3; *.flac"),
                   ("All files", "*.*"))
    )
    global name
    pat = Path(pathtoqsng)
    name = pat.name
    #mus = pygame.mixer.music.load(pathtoqsng)
    MainProgAlb()
def MainProgAlb():
    global pathtoqsng
    global pathtosng
    global inQueue
    pathtosng=pathtoqsng
    pygame.mixer.music.queue(pathtoqsng)
    inQueue=1
def YesOvr():
    pathtosng=pathtoqsng
    pygame.mixer.music.queue(pathtoqsng)
    inQueue=1

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
    global inQueue
    global taglen
    tottime=taglen
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
taglen=0
def MainProg2():
    global inQueue
    if inQueue==0:
        tag = TinyTag.get(pathtosng, image=True)
    else:
        tag = TinyTag.get(pathtoqsng, image=True)
        inQueue = 0
    global taglen
    taglen=tag.duration
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
    button3.configure(command=OpenFile2)
    global button
    DisplayGUIButton(button)
    slider.set(pygame.mixer.music.get_volume()*100)
    while True:
        ChkSongOver()
        updProgBar(progressbar, tag, elap,tot)

def MainProg():
    root.update()
    if pathtosng == "":
        while True:
            root.update()
    else:
        file_path = pathtosng
        filename = Path(file_path).stem
        print(filename)
        print(pathtosng)
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

def ChangeVol(val):
    pygame.mixer_music.set_volume(val/100)
    voltext.configure(text=math.trunc(val))
if mode==0:
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
    button2 = tk.CTkButton(root, text="📁", width=30, command=OpenFile)
    button2.place(relx=0.4, rely=0.85, anchor='c')
    button3 = tk.CTkButton(root, text="💿", width=30, command=OpenFile2)
    button3.place(relx=0.6, rely=0.85, anchor='c')
    slider=tk.CTkSlider(root, from_=0, to=100, command=ChangeVol,orientation='vertical')
    slider.place(relx=0.1, rely=0.4, anchor='c')
    slider.set(pygame.mixer.music.get_volume()*100)
    voltext = tk.CTkLabel(root, text="", font=("Arial", 17))
    voltext.place(relx=0.1, rely=0.65, anchor='c')
    voltext.configure(text=math.trunc(pygame.mixer.music.get_volume()*100))
    isEnd = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(isEnd)
    MainProg()
else:
    Video("video.mp4").preview()

