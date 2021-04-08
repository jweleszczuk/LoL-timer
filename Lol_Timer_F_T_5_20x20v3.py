# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:28:22 2020

@author: Jarosław Wełeszczuk
"""

import wx
import os
import math
import threading
import time
import sys
import pyaudio
import wave
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence,detect_nonsilent
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import numpy as np
from keras.models import load_model
from pydub.playback import _play_with_simpleaudio
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
fs = 44100  # Record at 44100 samples per second
channels=1
seconds = 3

aktualna_sciezka=os.getcwd()+"\\Grafiki_20x20\\"
model=load_model(os.getcwd()+"\\model_85_v2")
slownik={
    "czas_Flash": 270,  # w sekunadach
    "czas_Błysk": 270,
    "czas_Teleport": 378,
    "czas_Smite": 81,
    "czas_Porażenie": 81,
    "czas_Cleanse": 189,
    "czas_Oczyszczenie": 189,
    "czas_Heal": 216,
    "czas_Uzdrowienie": 216,
    "czas_Ignite": 162,
    "czas_Podpalenie": 162,
    "czas_Exhaust": 189,
    "czas_Wyczerpanie": 189,
    "czas_Clarity": 216,
    "czas_Czystość": 216,
    "czas_Ghost": 189,
    "czas_Duch": 189,
    "czas_Barrier": 162,
    "czas_Bariera": 162,
    "spis_pozycji": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "czas_gry":1
    }
slownik_pozycji={'Aatrox': 0,
 'Ahri': 1,
 'Akali': 2,
 'Alistar': 3,
 'Amumu': 4,
 'Anivia': 5,
 'Annie': 6,
 'Aphelios': 7,
 'Ashe': 8,
 'Aurelion_Sol': 9,
 'Azir': 10,
 'Bard': 11,
 'Bariera': 12,
 'Barrier': 13,
 'Blitzcrank': 14,
 'Brand': 15,
 'Braum': 16,
 'Błysk': 17,
 'Caitlyn': 18,
 'Camille': 19,
 'Cassiopeia': 20,
 'ChoGath': 21,
 'Clarity': 22,
 'Cleanse': 23,
 'Corki': 24,
 'Czystość': 25,
 'Darius': 26,
 'Diana': 27,
 'Draven': 28,
 'Dr_Mundo': 29,
 'Duch': 30,
 'Ekko': 31,
 'Elise': 32,
 'Evelynn': 33,
 'Exhaust': 34,
 'Ezreal': 35,
 'Fiddlesticks': 36,
 'Fiora': 37,
 'Fizz': 38,
 'Flash': 39,
 'Galio': 40,
 'Gangplank': 41,
 'Garen': 42,
 'Ghost': 43,
 'Gnar': 44,
 'Gragas': 45,
 'Graves': 46,
 'Heal': 47,
 'Hecarim': 48,
 'Heimerdinger': 49,
 'Ignite': 50,
 'Illaoi': 51,
 'Irelia': 52,
 'Ivern': 53,
 'Janna': 54,
 'Jarvan': 55,
 'Jax': 56,
 'Jayce': 57,
 'Jhin': 58,
 'Jinx': 59,
 'Kai_Sa': 60,
 'Kalista': 61,
 'Karma': 62,
 'Karthus': 63,
 'Kassadin': 64,
 'Katarina': 65,
 'Kayle': 66,
 'Kayn': 67,
 'Kennen': 68,
 'Kha_Zix': 69,
 'Kindred': 70,
 'Kled': 71,
 'Kog_Maw': 72,
 'LeBlanc': 73,
 'Lee_Sin': 74,
 'Leona': 75,
 'Lillia': 76,
 'Lissandra': 77,
 'Lucian': 78,
 'Lulu': 79,
 'Lux': 80,
 'Malphite': 81,
 'Malzahar': 82,
 'Maokai': 83,
 'Master_Yi': 84,
 'Miss_Fortune': 85,
 'Mordekaiser': 86,
 'Morgana': 87,
 'Nami': 88,
 'Nasus': 89,
 'Nautilus': 90,
 'Neeko': 91,
 'Nidalee': 92,
 'Nocturne': 93,
 'Nunu': 94,
 'Oczyszczenie': 95,
 'Olaf': 96,
 'Orianna': 97,
 'Ornn': 98,
 'Pantheon': 99,
 'Podpalenie': 100,
 'Poppy': 101,
 'Porażenie': 102,
 'Pyke': 103,
 'Qiyana': 104,
 'Quinn': 105,
 'Rakan': 106,
 'Rammus': 107,
 'Rek_Sai': 108,
 'Renekton': 109,
 'Rengar': 110,
 'Riven': 111,
 'Rumble': 112,
 'Ryze': 113,
 'Samira': 114,
 'Sejuani': 115,
 'Senna': 116,
 'Sett': 117,
 'Shaco': 118,
 'Shen': 119,
 'Shyvana': 120,
 'Singed': 121,
 'Sion': 122,
 'Sivir': 123,
 'Skarner': 124,
 'Smite': 125,
 'Sona': 126,
 'Soraka': 127,
 'Swain': 128,
 'Sylas': 129,
 'Syndra': 130,
 'Tahm_Kench': 131,
 'Taliyah': 132,
 'Talon': 133,
 'Taric': 134,
 'Teemo': 135,
 'Teleport': 136,
 'Thresh': 137,
 'Tristana': 138,
 'Trundle': 139,
 'Tryndamere': 140,
 'Twisted_Fate': 141,
 'Twitch': 142,
 'Udyr': 143,
 'Urgot': 144,
 'Uzdrowienie': 145,
 'Varus': 146,
 'Vayne': 147,
 'Veigar': 148,
 'Vel_Koz': 149,
 'Vi': 150,
 'Viktor': 151,
 'Vladimir': 152,
 'Volibear': 153,
 'Warwick': 154,
 'Wukong': 155,
 'Wyczerpanie': 156,
 'Xayah': 157,
 'Xerath': 158,
 'Xin_Zhao': 159,
 'Yasuo': 160,
 'Yorick': 161,
 'Yone': 162,
 'Yuumi': 163,
 'Zac': 164,
 'Zed': 165,
 'Ziggs': 166,
 'Zilean': 167,
 'Zoe': 168,
 'Zyra': 169}

l_poz_p=[
(99, 50 ),
(99, 80 ),
(99, 110 ),
(99, 140 ),
(99, 170 ),
(99, 200 ),
(99, 230 ),
(99, 260 ),
(99, 290 ),
(99, 320 ),
(99, 350 ),
    ]
l_poz_cd=[

(53, 55 ),
(53, 85 ),
(53, 115 ),
(53, 145 ),
(53, 175 ),
(53, 205 ),
(53, 235 ),
(53, 265 ),
(53, 295 ),
(53, 325 ),
(53, 355 ),
    ]
l_poz_vats=[
(75, 50 ),
(75, 80 ),
(75, 110 ),
(75, 140 ),
(75, 170 ),
(75, 200 ),
(75, 230 ),
(75, 260 ),
(75, 290 ),
(75, 320 ),
(75, 350 ),
    ]
l_poz_b=[
(5, 50 ),
(5, 80 ),
(5, 110 ),
(5, 140 ),
(5, 170 ),
(5, 200 ),
(5, 230 ),
(5, 260 ),
(5, 290 ),
(5, 320 ),
(5, 350 ),
    ]
l_poz_s=[
(30, 50 ),
(30, 80 ),
(30, 110 ),
(30, 140 ),
(30, 170 ),
(30, 200 ),
(30, 230 ),
(30, 260 ),
(30, 290 ),
(30, 320 ),
(30, 350 ),
    ]
def nagraj():

    filename = "plik.wav"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    
    frames = []  # Initialize array to store frames
    print("Start")
    # Store data in chunks for X seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print("Stop")
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    p.terminate
def podziel_nagranie_na_ciszy():
    db=[
        -25,
        -30,
        -35,
        ]
    ms=[200,
        300,
        400
        ]
    rezults=[]  
    song = AudioSegment.from_mp3("plik.wav")
    for y in ms:
        for x in db:
            chunks =split_on_silence(
                    song, 
                    min_silence_len = y,
                    silence_thresh = x, #dopasować
                    keep_silence=True)
            if len(chunks)==2:
                for t in range(len(chunks)):
                    chunks[t].export(os.getcwd()+"\Podział_"+str(t)+".wav", format="wav")
            break
        break
        
def wydluz_do_jednej_dlugosci():
    lista_dzwiekow=[ 
    "Podział_0.wav",
    "Podział_1.wav"
    ]
     
    l_dl=[]
    for x in lista_dzwiekow:
        z=AudioSegment.from_mp3(x)
        l_dl.append(z)
    dl_max=3000
    
    for x in range(len(l_dl)):
        c=len(l_dl[x])
        braki=dl_max-c
        #print(c,braki)
        b_segment = AudioSegment.silent(duration=braki)  #duration in milliseconds
        final_song = b_segment + l_dl[x]
        final_song.export(os.getcwd()+"\Podział_pop"+str(x) +".wav", format="wav")
        
def stworz_waveform():
    lista_dzwiekow=[ 
    "Podział_pop0.wav",
    "Podział_pop1.wav"
    ]
           
    f = plt.figure()
    for x in range(len(lista_dzwiekow)):
       z=wave.open(os.getcwd()+"/"+lista_dzwiekow[x],"r")
       signal = z.readframes(-1)
       signal = np.frombuffer(signal,dtype= "int16")
       plt.plot(signal,color='black')                 
       plt.ylim(-14000,14000)
       plt.title("")
       plt.axis('off')
       plt.savefig(os.getcwd()+"\o_"+lista_dzwiekow[x].split(".")[0], dpi=None, facecolor=None, edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)
       plt.close()


        
class Okno_glowne(wx.Frame):
    def __init__(self, parent=None):
        super(Okno_glowne, self).__init__(parent)
        
        self.SetTitle("LoL_Timer")
        self.Size=(140,460)
        self.SetPosition((5,400))
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.SetWindowStyle(wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.STAY_ON_TOP)
        self.panel=wx.Panel(self, wx.ID_ANY)
        Okno_glowne.Przycisk_0 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[0][0],l_poz_p[0][1]),size=(20,20))
        Okno_glowne.Przycisk_0.Bind(wx.EVT_BUTTON,self.wyczysz_0)
        Okno_glowne.Przycisk_1 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[1][0],l_poz_p[1][1]),size=(20,20))
        Okno_glowne.Przycisk_1.Bind(wx.EVT_BUTTON,self.wyczysz_1)
        Okno_glowne.Przycisk_2 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[2][0],l_poz_p[2][1]),size=(20,20))
        Okno_glowne.Przycisk_2.Bind(wx.EVT_BUTTON,self.wyczysz_2)
        Okno_glowne.Przycisk_3 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[3][0],l_poz_p[3][1]),size=(20,20))
        Okno_glowne.Przycisk_3.Bind(wx.EVT_BUTTON,self.wyczysz_3)
        Okno_glowne.Przycisk_4 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[4][0],l_poz_p[4][1]),size=(20,20))
        Okno_glowne.Przycisk_4.Bind(wx.EVT_BUTTON,self.wyczysz_4)
        Okno_glowne.Przycisk_5 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[5][0],l_poz_p[5][1]),size=(20,20))
        Okno_glowne.Przycisk_5.Bind(wx.EVT_BUTTON,self.wyczysz_5)
        Okno_glowne.Przycisk_6 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[6][0],l_poz_p[6][1]),size=(20,20))
        Okno_glowne.Przycisk_6.Bind(wx.EVT_BUTTON,self.wyczysz_6)
        Okno_glowne.Przycisk_7 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[7][0],l_poz_p[7][1]),size=(20,20))
        Okno_glowne.Przycisk_7.Bind(wx.EVT_BUTTON,self.wyczysz_7)
        Okno_glowne.Przycisk_8 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[8][0],l_poz_p[8][1]),size=(20,20))
        Okno_glowne.Przycisk_8.Bind(wx.EVT_BUTTON,self.wyczysz_8)
        Okno_glowne.Przycisk_9 = wx.Button(self.panel,-1,"X",pos=(l_poz_p[9][0],l_poz_p[9][1]),size=(20,20))
        Okno_glowne.Przycisk_9.Bind(wx.EVT_BUTTON,self.wyczysz_9)
        
        Okno_glowne.Przycisk_14=wx.Button(self.panel,-1,"Start_Timer",pos=(3,345),size=(120,20,))
        Okno_glowne.Przycisk_14.Bind(wx.EVT_BUTTON,self.start_time)
        
        Okno_glowne.Przycisk_15=wx.Button(self.panel,-1,"Set_Timer",pos=(3,365),size=(60,20,))
        Okno_glowne.Przycisk_15.Bind(wx.EVT_BUTTON,self.change_time)
        Okno_glowne.Pole_tekstowe_2 = wx.TextCtrl(self.panel,-1,pos=(68,365),size=(55,20))
        Okno_glowne.Przycisk_15.Hide()
        Okno_glowne.Pole_tekstowe_2.Hide()
        
        l_p = wx.StaticText(self.panel, -1, 'Lux,Flash,04;21', (3, 3))
        Okno_glowne.text0t=wx.StaticText(self.panel,-1,"--;--",pos=(92,3))
        Okno_glowne.Pole_tekstowe_1 = wx.TextCtrl(self.panel,-1,pos=(1,20),size=(95,24))

        Okno_glowne.Przycisk_11 = wx.Button(self.panel,-1,"K",pos=(100,20),size=(20,25))
        
        Okno_glowne.Przycisk_11.Bind(wx.EVT_BUTTON,self.wczytaj_wpis_2)
        Okno_glowne.Przycisk_11.Hide()
        
        ctrlq_id=wx.NewIdRef(count=1)
        self.Bind(wx.EVT_MENU,self.test_przycisku_ctrl_q,id=ctrlq_id)
        
        ctrls_id=wx.NewIdRef(count=1)
        self.Bind(wx.EVT_MENU,self.test_przycisku_ctrl_s,id=ctrls_id)
        
        self.accel_tbl=wx.AcceleratorTable([
            (wx.ACCEL_CTRL,ord('Q'),ctrlq_id), #rozpocznij przechwytywanie głosowe
            (wx.ACCEL_CTRL,ord('S'),ctrls_id), #dodaj wpis
            
            ])
        self.SetAcceleratorTable(self.accel_tbl)
        
        Okno_glowne.text0k = wx.StaticText(self.panel, -1, 'c_0', (l_poz_cd[0][0],l_poz_cd[0][1]))
        Okno_glowne.text1k = wx.StaticText(self.panel, -1, 'c_1', (l_poz_cd[1][0],l_poz_cd[1][1]))
        Okno_glowne.text2k = wx.StaticText(self.panel, -1, 'c_2', (l_poz_cd[2][0],l_poz_cd[2][1]))
        Okno_glowne.text3k = wx.StaticText(self.panel, -1, 'c_3', (l_poz_cd[3][0],l_poz_cd[3][1]))
        Okno_glowne.text4k = wx.StaticText(self.panel, -1, 'c_4', (l_poz_cd[4][0],l_poz_cd[4][1]))
        Okno_glowne.text5k = wx.StaticText(self.panel, -1, 'c_5', (l_poz_cd[5][0],l_poz_cd[5][1]))
        Okno_glowne.text6k = wx.StaticText(self.panel, -1, 'c_6', (l_poz_cd[6][0],l_poz_cd[6][1]))
        Okno_glowne.text7k = wx.StaticText(self.panel, -1, 'c_7', (l_poz_cd[7][0],l_poz_cd[7][1]))
        Okno_glowne.text8k = wx.StaticText(self.panel, -1, 'c_8', (l_poz_cd[8][0],l_poz_cd[8][1]))
        Okno_glowne.text9k = wx.StaticText(self.panel, -1, 'c_9', (l_poz_cd[9][0],l_poz_cd[9][1]))
        
        
        
        imageFile0=aktualna_sciezka+"0_s.jpg"
        imageFile1=aktualna_sciezka+"0_s.jpg"
        imageFile2=aktualna_sciezka+"0_s.jpg"
        imageFile3=aktualna_sciezka+"0_s.jpg"
        imageFile4=aktualna_sciezka+"0_s.jpg"
        imageFile5=aktualna_sciezka+"0_s.jpg"
        imageFile6=aktualna_sciezka+"0_s.jpg"
        imageFile7=aktualna_sciezka+"0_s.jpg"
        imageFile8=aktualna_sciezka+"0_s.jpg"
        imageFile9=aktualna_sciezka+"0_s.jpg"

        image0 = wx.Bitmap(imageFile0, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap0 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image0),pos=(l_poz_vats[0][0],l_poz_vats[0][1]),size=(20,20))
        image1 = wx.Bitmap(imageFile1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image1),pos=(l_poz_vats[1][0],l_poz_vats[1][1]),size=(20,20))
        image2 = wx.Bitmap(imageFile2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image2),pos=(l_poz_vats[2][0],l_poz_vats[2][1]),size=(20,20))
        image3 = wx.Bitmap(imageFile3, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap3 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image3),pos=(l_poz_vats[3][0],l_poz_vats[3][1]),size=(20,20))
        image4 = wx.Bitmap(imageFile4, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap4 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image4),pos=(l_poz_vats[4][0],l_poz_vats[4][1]),size=(20,20))
        image5 = wx.Bitmap(imageFile5, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap5 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image5),pos=(l_poz_vats[5][0],l_poz_vats[5][1]),size=(20,20))
        image6 = wx.Bitmap(imageFile6, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap6 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image6),pos=(l_poz_vats[6][0],l_poz_vats[6][1]),size=(20,20))
        image7 = wx.Bitmap(imageFile7, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap7 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image7),pos=(l_poz_vats[7][0],l_poz_vats[7][1]),size=(20,20))
        image8 = wx.Bitmap(imageFile8, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap8 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image8),pos=(l_poz_vats[8][0],l_poz_vats[8][1]),size=(20,20))
        image9 = wx.Bitmap(imageFile9, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap9 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image9),pos=(l_poz_vats[9][0],l_poz_vats[9][1]),size=(20,20))
        imageFile0_1=aktualna_sciezka+"Empty.jpg"
        imageFile0_2=aktualna_sciezka+"Empty.jpg"
        imageFile1_1=aktualna_sciezka+"Empty.jpg"
        imageFile1_2=aktualna_sciezka+"Empty.jpg"
        imageFile2_1=aktualna_sciezka+"Empty.jpg"
        imageFile2_2=aktualna_sciezka+"Empty.jpg"
        imageFile3_1=aktualna_sciezka+"Empty.jpg"
        imageFile3_2=aktualna_sciezka+"Empty.jpg"
        imageFile4_1=aktualna_sciezka+"Empty.jpg"
        imageFile4_2=aktualna_sciezka+"Empty.jpg"
        imageFile5_1=aktualna_sciezka+"Empty.jpg"
        imageFile5_2=aktualna_sciezka+"Empty.jpg"
        imageFile6_1=aktualna_sciezka+"Empty.jpg"
        imageFile6_2=aktualna_sciezka+"Empty.jpg"
        imageFile7_1=aktualna_sciezka+"Empty.jpg"
        imageFile7_2=aktualna_sciezka+"Empty.jpg"
        imageFile8_1=aktualna_sciezka+"Empty.jpg"
        imageFile8_2=aktualna_sciezka+"Empty.jpg"
        imageFile9_1=aktualna_sciezka+"Empty.jpg"
        imageFile9_2=aktualna_sciezka+"Empty.jpg"
        image0_1 = wx.Bitmap(imageFile0_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap0_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image0_1),pos=(l_poz_b[0][0],l_poz_b[0][1]),size=(20,20))
        image0_2 = wx.Bitmap(imageFile0_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap0_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image0_2),pos=(l_poz_s[0][0],l_poz_s[0][1]),size=(20,20))
        image1_1 = wx.Bitmap(imageFile1_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap1_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image1_1),pos=(l_poz_b[1][0],l_poz_b[1][1]),size=(20,20))
        image1_2 = wx.Bitmap(imageFile1_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap1_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image1_2),pos=(l_poz_s[1][0],l_poz_s[1][1]),size=(20,20))
        image2_1 = wx.Bitmap(imageFile2_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap2_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image2_1),pos=(l_poz_b[2][0],l_poz_b[2][1]),size=(20,20))
        image2_2 = wx.Bitmap(imageFile2_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap2_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image2_2),pos=(l_poz_s[2][0],l_poz_s[2][1]),size=(20,20))
        image3_1 = wx.Bitmap(imageFile3_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap3_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image3_1),pos=(l_poz_b[3][0],l_poz_b[3][1]),size=(20,20))
        image3_2 = wx.Bitmap(imageFile3_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap3_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image3_2),pos=(l_poz_s[3][0],l_poz_s[3][1]),size=(20,20))
        image4_1 = wx.Bitmap(imageFile4_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap4_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image4_1),pos=(l_poz_b[4][0],l_poz_b[4][1]),size=(20,20))
        image4_2 = wx.Bitmap(imageFile4_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap4_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image4_2),pos=(l_poz_s[4][0],l_poz_s[4][1]),size=(20,20))
        image5_1 = wx.Bitmap(imageFile5_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap5_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image5_1),pos=(l_poz_b[5][0],l_poz_b[5][1]),size=(20,20))
        image5_2 = wx.Bitmap(imageFile5_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap5_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image5_2),pos=(l_poz_s[5][0],l_poz_s[5][1]),size=(20,20))
        image6_1 = wx.Bitmap(imageFile6_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap6_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image6_1),pos=(l_poz_b[6][0],l_poz_b[6][1]),size=(20,20))
        image6_2 = wx.Bitmap(imageFile6_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap6_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image6_2),pos=(l_poz_s[6][0],l_poz_s[6][1]),size=(20,20))
        image7_1 = wx.Bitmap(imageFile7_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap7_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image7_1),pos=(l_poz_b[7][0],l_poz_b[7][1]),size=(20,20))
        image7_2 = wx.Bitmap(imageFile7_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap7_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image7_2),pos=(l_poz_s[7][0],l_poz_s[7][1]),size=(20,20))
        image8_1 = wx.Bitmap(imageFile8_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap8_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image8_1),pos=(l_poz_b[8][0],l_poz_b[8][1]),size=(20,20))
        image8_2 = wx.Bitmap(imageFile8_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap8_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image8_2),pos=(l_poz_s[8][0],l_poz_s[8][1]),size=(20,20))
        image9_1 = wx.Bitmap(imageFile9_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap9_1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image9_1),pos=(l_poz_b[0][0],l_poz_b[9][1]),size=(20,20))
        image9_2 = wx.Bitmap(imageFile9_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap9_2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(image9_2),pos=(l_poz_s[9][0],l_poz_s[9][1]),size=(20,20))
        
        l_dk = wx.StaticText(self.panel, -1, 'Jarosław Wełeszczuk\n\t07.2020r.', (5, 390))
        
        self.Show(True)
        
    def test_przycisku_ctrl_q(self,evt):
        pass

        
    def test_przycisku_ctrl_s(self,evt):
        self.wczytaj_wpis()
        Okno_glowne.Pole_tekstowe_1.Clear()
    
    def start_time(self,evt):
        Okno_glowne.Przycisk_15.Show()
        Okno_glowne.Przycisk_14.Hide()
        Okno_glowne.Pole_tekstowe_2.Show()
        Okno_glowne.Przycisk_11.Show()
        self.zacznij_czas_gry()

        
    def change_time(self,evt):
        z=Okno_glowne.Pole_tekstowe_2.GetValue()
        if len(z)==5:
            Okno_glowne.Pole_tekstowe_2.Clear()
            wart=self.przelicz_wpis_na_sekundy(z)
            slownik["czas_gry"]=wart
   
    def przelicz_wpis_na_sekundy(self,wartosc):
        czas_uzycia=wartosc.split(";")
        sekundy=(int(czas_uzycia[0])*60 + int(czas_uzycia[1]))
        czas_w_sekundach=sekundy
        return czas_w_sekundach

    def przelicz_sekundy_na_wpis(self,wartosc):
        czas_w_minutach=round(wartosc/60,2) 
        t_sek,t_min=math.modf(czas_w_minutach) 
        t_min=(str(t_min)).split(".")
        t_min=t_min[0]
        t_sek=str(round((t_sek*60),0)) 
        t_sek=t_sek.split(".")
        t_sek=t_sek[0]
        if len(t_sek)==1:
            t_sek="0"+t_sek
        t_min=str(t_min)
        if len(t_min)==1:
            t_min="0"+t_min
        odpowiednik=str(t_min)+";"+t_sek
        return odpowiednik
    
    def p_0(self,evt):
        pass

    
    def wyczysz_0(self,evt):
        self.w_0()

    def wyczysz_1(self,evt):
        self.w_1()

    def wyczysz_2(self,evt):
        self.w_2()

    def wyczysz_3(self,evt):
        self.w_3()

    def wyczysz_4(self,evt):
        self.w_4()

    def wyczysz_5(self,evt):
        self.w_5()

    def wyczysz_6(self,evt):
        self.w_6()

    def wyczysz_7(self,evt):
        self.w_7()

    def wyczysz_8(self,evt):
        self.w_8()

    def wyczysz_9(self,evt):
        self.w_9()

    def w_0(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap0.SetBitmap(wx.Bitmap(image))
        imageFile0_1=aktualna_sciezka+"Empty.jpg"
        imageFile0_2=aktualna_sciezka+"Empty.jpg"
        image0_1 = wx.Bitmap(imageFile0_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap0_1.SetBitmap(wx.Bitmap(image0_1))
        image0_2 = wx.Bitmap(imageFile0_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap0_2.SetBitmap(wx.Bitmap(image0_2))
        Okno_glowne.text0k.SetLabel("c_0")
        slownik["spis_pozycji"].append(0)
        try:
            Okno_glowne.zatrzymaj_watek(self,0)
        except: 
            pass

    def w_1(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap1.SetBitmap(wx.Bitmap(image))
        imageFile1_1=aktualna_sciezka+"Empty.jpg"
        imageFile1_2=aktualna_sciezka+"Empty.jpg"
        image1_1 = wx.Bitmap(imageFile1_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap1_1.SetBitmap(wx.Bitmap(image1_1))
        image1_2 = wx.Bitmap(imageFile1_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap1_2.SetBitmap(wx.Bitmap(image1_2))
        Okno_glowne.text1k.SetLabel("c_1")
        slownik["spis_pozycji"].append(1)
        try:
            Okno_glowne.zatrzymaj_watek(self,1)
        except: 
            pass
        
    def w_2(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap2.SetBitmap(wx.Bitmap(image))
        imageFile2_1=aktualna_sciezka+"Empty.jpg"
        imageFile2_2=aktualna_sciezka+"Empty.jpg"
        image2_1 = wx.Bitmap(imageFile2_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap2_1.SetBitmap(wx.Bitmap(image2_1))
        image2_2 = wx.Bitmap(imageFile2_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap2_2.SetBitmap(wx.Bitmap(image2_2))
        Okno_glowne.text2k.SetLabel("c_2")
        slownik["spis_pozycji"].append(2)
        try:
            Okno_glowne.zatrzymaj_watek(self,2)
        except: 
            pass

    def w_3(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap3.SetBitmap(wx.Bitmap(image))
        imageFile3_1=aktualna_sciezka+"Empty.jpg"
        imageFile3_2=aktualna_sciezka+"Empty.jpg"
        image3_1 = wx.Bitmap(imageFile3_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap3_1.SetBitmap(wx.Bitmap(image3_1))
        image3_2 = wx.Bitmap(imageFile3_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap3_2.SetBitmap(wx.Bitmap(image3_2))
        Okno_glowne.text3k.SetLabel("c_3")
        slownik["spis_pozycji"].append(3)
        try:
            Okno_glowne.zatrzymaj_watek(self,3)
        except: 
            pass

    def w_4(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap4.SetBitmap(wx.Bitmap(image))
        imageFile4_1=aktualna_sciezka+"Empty.jpg"
        imageFile4_2=aktualna_sciezka+"Empty.jpg"
        image4_1 = wx.Bitmap(imageFile4_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap4_1.SetBitmap(wx.Bitmap(image4_1))
        image4_2 = wx.Bitmap(imageFile4_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap4_2.SetBitmap(wx.Bitmap(image4_2))
        Okno_glowne.text4k.SetLabel("c_4")
        slownik["spis_pozycji"].append(4)
        try:
            Okno_glowne.zatrzymaj_watek(self,4)
        except: 
            pass

    def w_5(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap5.SetBitmap(wx.Bitmap(image))
        imageFile5_1=aktualna_sciezka+"Empty.jpg"
        imageFile5_2=aktualna_sciezka+"Empty.jpg"
        image5_1 = wx.Bitmap(imageFile5_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap5_1.SetBitmap(wx.Bitmap(image5_1))
        image5_2 = wx.Bitmap(imageFile5_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap5_2.SetBitmap(wx.Bitmap(image5_2))
        Okno_glowne.text5k.SetLabel("c_5")
        slownik["spis_pozycji"].append(5)
        try:
            Okno_glowne.zatrzymaj_watek(self,5)
        except: 
            pass

    def w_6(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap6.SetBitmap(wx.Bitmap(image))
        imageFile6_1=aktualna_sciezka+"Empty.jpg"
        imageFile6_2=aktualna_sciezka+"Empty.jpg"
        image6_1 = wx.Bitmap(imageFile6_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap6_1.SetBitmap(wx.Bitmap(image6_1))
        image6_2 = wx.Bitmap(imageFile6_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap6_2.SetBitmap(wx.Bitmap(image6_2))
        Okno_glowne.text6k.SetLabel("c_6")
        slownik["spis_pozycji"].append(6)
        try:
            Okno_glowne.zatrzymaj_watek(self,6)
        except: 
            pass

    def w_7(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap7.SetBitmap(wx.Bitmap(image))
        imageFile7_1=aktualna_sciezka+"Empty.jpg"
        imageFile7_2=aktualna_sciezka+"Empty.jpg"
        image7_1 = wx.Bitmap(imageFile7_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap7_1.SetBitmap(wx.Bitmap(image7_1))
        image7_2 = wx.Bitmap(imageFile7_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap7_2.SetBitmap(wx.Bitmap(image7_2))
        Okno_glowne.text7k.SetLabel("c_7")
        slownik["spis_pozycji"].append(7)
        try:
            Okno_glowne.zatrzymaj_watek(self,7)
        except: 
            pass

    def w_8(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap8.SetBitmap(wx.Bitmap(image))
        imageFile8_1=aktualna_sciezka+"Empty.jpg"
        imageFile8_2=aktualna_sciezka+"Empty.jpg"
        image8_1 = wx.Bitmap(imageFile8_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap8_1.SetBitmap(wx.Bitmap(image8_1))
        image8_2 = wx.Bitmap(imageFile8_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap8_2.SetBitmap(wx.Bitmap(image8_2))
        Okno_glowne.text8k.SetLabel("c_8")
        slownik["spis_pozycji"].append(8)
        try:
            Okno_glowne.zatrzymaj_watek(self,8)
        except: 
            pass

    def w_9(self):
        image=aktualna_sciezka+"0_s.jpg"
        Okno_glowne.imageBitmap9.SetBitmap(wx.Bitmap(image))
        imageFile9_1=aktualna_sciezka+"Empty.jpg"
        imageFile9_2=aktualna_sciezka+"Empty.jpg"
        image9_1 = wx.Bitmap(imageFile9_1, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap9_1.SetBitmap(wx.Bitmap(image9_1))
        image9_2 = wx.Bitmap(imageFile9_2, wx.BITMAP_TYPE_ANY)
        Okno_glowne.imageBitmap9_2.SetBitmap(wx.Bitmap(image9_2))
        Okno_glowne.text9k.SetLabel("c_9")
        slownik["spis_pozycji"].append(9)
        try:
            Okno_glowne.zatrzymaj_watek(self,9)
        except: 
            pass

    def test_do_zmien_bohatera(self,nazwa):
        plik_bohatera=nazwa+".jpg"
        pula=os.listdir(aktualna_sciezka)
        if plik_bohatera not in pula:
            cos=(False,"Unkown.jpg")
            return cos
        else:
            cos=(True,plik_bohatera)
            return cos

    def test_do_zmien_czar(self,czar):
        plik_czaru=czar+".jpg"
        pula=os.listdir(aktualna_sciezka)
        if plik_czaru not in pula:
            cos=(False,"Unkown.jpg")
            return cos
        else:
            cos=(True,plik_czaru)
            return cos

    def zmien_bohatera(self,pozycja,plik_bohatera):
        plik_bohatera=aktualna_sciezka+plik_bohatera
        image = wx.Bitmap(plik_bohatera, wx.BITMAP_TYPE_ANY)
        if pozycja ==0:
            Okno_glowne.imageBitmap0_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==1:
            Okno_glowne.imageBitmap1_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==2:
            Okno_glowne.imageBitmap2_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==3:
            Okno_glowne.imageBitmap3_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==4:
            Okno_glowne.imageBitmap4_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==5:
            Okno_glowne.imageBitmap5_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==6:
            Okno_glowne.imageBitmap6_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==7:
            Okno_glowne.imageBitmap7_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==8:
            Okno_glowne.imageBitmap8_1.SetBitmap(wx.Bitmap(image))
        elif pozycja==9:
            Okno_glowne.imageBitmap9_1.SetBitmap(wx.Bitmap(image))

    def zmien_czar(self,pozycja,plik_czaru):
        plik_czaru=aktualna_sciezka+plik_czaru
        image = wx.Bitmap(plik_czaru, wx.BITMAP_TYPE_ANY)
        if pozycja ==0:
            Okno_glowne.imageBitmap0_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==1:
            Okno_glowne.imageBitmap1_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==2:
            Okno_glowne.imageBitmap2_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==3:
            Okno_glowne.imageBitmap3_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==4:
            Okno_glowne.imageBitmap4_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==5:
            Okno_glowne.imageBitmap5_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==6:
            Okno_glowne.imageBitmap6_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==7:
            Okno_glowne.imageBitmap7_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==8:
            Okno_glowne.imageBitmap8_2.SetBitmap(wx.Bitmap(image))
        elif pozycja==9:
            Okno_glowne.imageBitmap9_2.SetBitmap(wx.Bitmap(image))

    def zmien_czas_odnowienia_cd(self,pozycja,wartosc):
        if pozycja==0:
            Okno_glowne.text0k.SetLabel(wartosc)
        elif pozycja==1:
            Okno_glowne.text1k.SetLabel(wartosc)
        elif pozycja==2:
            Okno_glowne.text2k.SetLabel(wartosc)
        elif pozycja==3:
            Okno_glowne.text3k.SetLabel(wartosc)
        elif pozycja==4:
            Okno_glowne.text4k.SetLabel(wartosc)
        elif pozycja==5:
            Okno_glowne.text5k.SetLabel(wartosc)
        elif pozycja==6:
            Okno_glowne.text6k.SetLabel(wartosc)
        elif pozycja==7:
            Okno_glowne.text7k.SetLabel(wartosc)
        elif pozycja==8:
            Okno_glowne.text8k.SetLabel(wartosc)
        elif pozycja==9:
            Okno_glowne.text9k.SetLabel(wartosc)

    def zmien_kolor_vats(self,pozycja,image):
        if pozycja ==0:
            Okno_glowne.imageBitmap0.SetBitmap(wx.Bitmap(image))
        elif pozycja==1:
            Okno_glowne.imageBitmap1.SetBitmap(wx.Bitmap(image))
        elif pozycja==2:
            Okno_glowne.imageBitmap2.SetBitmap(wx.Bitmap(image))
        elif pozycja==3:
            Okno_glowne.imageBitmap3.SetBitmap(wx.Bitmap(image))
        elif pozycja==4:
            Okno_glowne.imageBitmap4.SetBitmap(wx.Bitmap(image))
        elif pozycja==5:
            Okno_glowne.imageBitmap5.SetBitmap(wx.Bitmap(image))
        elif pozycja==6:
            Okno_glowne.imageBitmap6.SetBitmap(wx.Bitmap(image))
        elif pozycja==7:
            Okno_glowne.imageBitmap7.SetBitmap(wx.Bitmap(image))
        elif pozycja==8:
            Okno_glowne.imageBitmap8.SetBitmap(wx.Bitmap(image))
        elif pozycja==9:
            Okno_glowne.imageBitmap9.SetBitmap(wx.Bitmap(image))

    def rozpocznij_watek(self,pozycja,wartosc):
        if pozycja ==0:
            Okno_glowne.thread0 = myThread(0,wartosc)
            Okno_glowne.thread0.start()
        elif pozycja==1:
            Okno_glowne.thread1 = myThread(1,wartosc)
            Okno_glowne.thread1.start()
        elif pozycja==2:
            Okno_glowne.thread2 = myThread(2,wartosc)
            Okno_glowne.thread2.start()
        elif pozycja==3:
            Okno_glowne.thread3 = myThread(3,wartosc)
            Okno_glowne.thread3.start()
        elif pozycja==4:
            Okno_glowne.thread4 = myThread(4,wartosc)
            Okno_glowne.thread4.start()
        elif pozycja==5:
            Okno_glowne.thread5 = myThread(5,wartosc)
            Okno_glowne.thread5.start()
        elif pozycja==6:
            Okno_glowne.thread6 = myThread(6,wartosc)
            Okno_glowne.thread6.start()
        elif pozycja==7:
            Okno_glowne.thread7 = myThread(7,wartosc)
            Okno_glowne.thread7.start()
        elif pozycja==8:
            Okno_glowne.thread8 = myThread(8,wartosc)
            Okno_glowne.thread8.start()
        elif pozycja==9:
            Okno_glowne.thread9 = myThread(9,wartosc)
            Okno_glowne.thread9.start()
            
    def zatrzymaj_watek(self,pozycja):
        if pozycja ==0:
            Okno_glowne.thread0.kill()
        elif pozycja==1:
            Okno_glowne.thread1.kill()
        elif pozycja==2:
            Okno_glowne.thread2.kill()
        elif pozycja==3:
            Okno_glowne.thread3.kill()
        elif pozycja==4:
            Okno_glowne.thread4.kill()
        elif pozycja==5:
            Okno_glowne.thread5.kill()
        elif pozycja==6:
            Okno_glowne.thread6.kill()
        elif pozycja==7:
            Okno_glowne.thread7.kill()
        elif pozycja==8:
            Okno_glowne.thread8.kill()
        elif pozycja==9:
            Okno_glowne.thread9.kill()
            
    def zacznij_czas_gry(self):
        Okno_glowne.thread_l = myThread_liczacy()
        Okno_glowne.thread_l.start()
        
    def zakoncz_liczenie_czasu(self):
        Okno_glowne.thread_l.kill()
            
    def wczytaj_wpis_2(self,evt):
        self.wczytaj_wpis()
        
    def wczytaj_wpis(self):
        text_z_pola=self.Pole_tekstowe_1.GetValue()
        text_z_pola=text_z_pola.replace(" ","")
        if len(text_z_pola)!=0:
            if len(slownik["spis_pozycji"])!=0: 
                pozycja=min(slownik["spis_pozycji"])
                lista_wyjsciowa=text_z_pola.split(",")
                bohater=lista_wyjsciowa[0]  
                if "_" in bohater: 
                    zmienna1=bohater.split("_")
                    if zmienna1[1][0].islower():
                        pomoc1=zmienna1[1][0].upper()
                        pomoc1=zmienna1[0]+"_"+pomoc1+zmienna1[1][1:]
                        bohater=pomoc1
                if bohater[0].islower():
                    b=bohater[0].upper()
                    b=b+bohater[1:]
                    bohater=b
                czar=lista_wyjsciowa[1]
                if czar[0].islower():
                    a=czar[0].upper()
                    a=a+czar[1:]
                    czar=a
                if len(text_z_pola.split(","))==2  : 
                    czas=Okno_glowne.text0t.GetLabel()
                    warunek_boh=self.test_do_zmien_bohatera(bohater)
                    warunek_czar=self.test_do_zmien_czar(czar)
                    if czas!="--;--" and warunek_boh[0]==True and warunek_czar[0]==True and "czas_"+czar in slownik:
                        self.zmien_bohatera(pozycja,warunek_boh[1])
                        self.zmien_czar(pozycja,warunek_czar[1])
                        self.zmien_czas_odnowienia_cd(pozycja,str(slownik["czas_"+czar]))
                        kolor=self.jaki_kolor_vats(slownik["czas_"+czar])
                        self.zmien_kolor_vats(pozycja, kolor)
                        self.rozpocznij_watek(pozycja,slownik["czas_"+czar])
                        slownik["spis_pozycji"].remove(pozycja) 
                if len(text_z_pola.split(","))==3 and text_z_pola.split(",")[2]!="":
                    czas=lista_wyjsciowa[2] # podany
                    warunek_boh=self.test_do_zmien_bohatera(bohater)
                    warunek_czar=self.test_do_zmien_czar(czar)
                    if czas!="--;--" and warunek_boh[0]==True and warunek_czar[0]==True and "czas_"+czar in slownik:
                        czas_1=self.przelicz_wpis_na_sekundy(czas) 
                        r_czas=abs(slownik["czas_gry"]-czas_1) 
                        czas=(slownik["czas_"+czar])-r_czas
                        self.zmien_bohatera(pozycja,warunek_boh[1])
                        self.zmien_czar(pozycja,warunek_czar[1])
                        self.zmien_czas_odnowienia_cd(pozycja,str(czas))
                        kolor=self.jaki_kolor_vats(slownik["czas_"+czar])
                        self.zmien_kolor_vats(pozycja, kolor)
                        self.rozpocznij_watek(pozycja,czas)
                        slownik["spis_pozycji"].remove(pozycja) 

    def jaki_kolor_vats(self,jaki_czas_s):
        if jaki_czas_s >180 or jaki_czas_s <=180:
            plik=aktualna_sciezka+"180_s.jpg"
        if jaki_czas_s <=120:
            plik=aktualna_sciezka+"120_s.jpg"
        if jaki_czas_s <= 60:
            plik=aktualna_sciezka+"60_s.jpg"
        return plik
    
    def zatrzymaj_wszystkie_watki(self):
        for x in range(0,10):
            self.zatrzymaj_watek(x)
    def OnClose(self, event):
        try:
            self.w_0()
            self.w_1()
            self.w_2()
            self.w_3()
            self.w_4()
            self.w_5()
            self.w_6()
            self.w_7()
            self.w_8()
            self.w_9()
            Okno_glowne.thread_l.kill()
        except:
            pass
        self.Destroy()  

class myThread (threading.Thread):
    def __init__(self, threadID, wartosc):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.wartosc = wartosc
       self.kolor=""
       self.killed = False
       
    def run(self):
       self.rozpocznij_time(self.threadID, self.wartosc)
     
    def rozpocznij_time(self,threadID, wartosc):
        while wartosc>0:
            time.sleep(1)
            wartosc -= 1
            self.kolor=Okno_glowne.jaki_kolor_vats(self,wartosc)
            Okno_glowne.zmien_czas_odnowienia_cd(self,threadID,str(wartosc))
            Okno_glowne.zmien_kolor_vats(self,threadID,self.kolor)
        self.apoptoza(threadID)

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run      
        threading.Thread.start(self)
    
    def __run(self):

        
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup
    
    def globaltrace(self, frame, why, arg):
        if why == 'call':
          return self.localtrace
        else:
          return None
      
    def localtrace(self, frame, why, arg):
        if self.killed:
          if why == 'line':
              raise SystemExit()
        return self.localtrace
    
    def kill(self):
        self.killed = True
        
    def apoptoza(self,ID):
        if ID==0:
            Okno_glowne.w_0(self)
        elif ID==1:
            Okno_glowne.w_1(self)
        elif ID==2:
            Okno_glowne.w_2(self)
        elif ID==3:
            Okno_glowne.w_3(self)
        elif ID==4:
            Okno_glowne.w_4(self)
        elif ID==5:
            Okno_glowne.w_5(self)
        elif ID==6:
            Okno_glowne.w_6(self)
        elif ID==7:
            Okno_glowne.w_7(self)
        elif ID==8:
            Okno_glowne.w_8(self)
        elif ID==9:
            Okno_glowne.w_9(self)
            
class myThread_liczacy (threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self)
       self.killed = False
       
    def run(self):
       self.licz_time()
     
    def licz_time(self):
        while True:
            time.sleep(1)
            wpis=Okno_glowne.przelicz_sekundy_na_wpis(self,slownik["czas_gry"])
            slownik["czas_gry"]=slownik["czas_gry"]+1
            Okno_glowne.text0t.SetLabel(wpis)
            
    def start(self):
        self.__run_backup = self.run
        self.run = self.__run     
        threading.Thread.start(self)
    
    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup
    
    def globaltrace(self, frame, why, arg):
        if why == 'call':
          return self.localtrace
        else:
          return None
      
    def localtrace(self, frame, why, arg):
        if self.killed:
          if why == 'line':
              raise SystemExit()
        return self.localtrace
    
    def kill(self):
        self.killed = True
        
            
        
if __name__ == '__main__':

    app = wx.App()
    ex = Okno_glowne()
    ex.Show()
    app.MainLoop()
