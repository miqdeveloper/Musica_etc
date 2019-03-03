# -*- coding: utf-8 -*-
#!/usr/bin/python
from pytube  import YouTube
from pytube  import Playlist
from pydub import AudioSegment
import glob, os, time 
from  tqdm  import *




a = open("lista.txt","r")
try:
  for i in a.readlines():
    yt = i
    ur = YouTube(yt)
    tt = ur.title
    ck =ur.thumbnail_url
    tk = ur.streams.get_by_itag(140)
    print("Baixando...")
    print(tt)
    tk.download()
except Exception:
   print("\n")



for i in glob.glob('*.mp4'):
    ta = os.path.getsize(i)
    f = (ta * 8)
    sound = AudioSegment.from_file(i)
    a = i.replace(".mp4", ".mp3")
    print(sound.export(a, format="mp3"))

os.system("rm -rf *.mp4 && clear")

exit()
