# -*- coding: utf-8 -*-
#!/usr/bin/python3
from pytube  import YouTube
from pytube  import Playlist
from pydub import AudioSegment
import glob, os, time
import platform


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

    con = sound.export(a, format="mp3")
    print(con)
if platform.system() == "Linux":
   for del in glob.glob('*.mp4'):
    os.remove(del)
    
if platform.system() == "Windows":
  for i in glob.glob('*.mp4'):
    os.remove(i)

exit()
