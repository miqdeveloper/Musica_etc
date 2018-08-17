# -*- coding: utf-8 -*-
#Devidos créditos Miqueias
#https://www.facebook.com/miqueias.costa.754
from pytube  import YouTube
from pytube  import Playlist

print ("deseja baixar uma playlist ou apenas musicas separadas")
print("Digite 1 para muscas separadas e 2 para playlist")

pl = int(input('Digite: '))

if (pl == 1):
     while True:
          print("Você escolheu musicas separadas.")
          yt = str(input('cole a URL do video: '))
          ur = YouTube(yt)
          tt = ur.title
          ck =ur.thumbnail_url
          tk = ur.streams.get_by_itag(140)
          print("Baixando...")
          print(tt)
          tk.download()

if (pl == 2):
     print("Você escolheu Playlis.")
     pt = str(input("Link da palylist para ser baixada: "))
     ply = Playlist(pt)
     print("Aguarde enquanto a plylist esta sendo baixada...")
     print("OBS: Tudo depende da sua internet.")
     ply.download_all()
     

else:
     print("By Miqueias <3")
     exit()
    

     
     


     



