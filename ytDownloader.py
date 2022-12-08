from pytube import YouTube
from sys import argv
title = input("Enter video Link")
yt = YouTube(title)
print("Title: ", yt.title)
yd = yt.streams.get_highest_resolution()
yd.download("/home/dnlsgv/Vídeos")
