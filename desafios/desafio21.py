""" 15/03/2020 jan Mesu
Faça um programa em python que abra e reproduza um audio de um arquivo em
MP3
"""
from pygame import mixer, init, event

init()
mixer.init()
mixer.music.load('desafio21.mp3')
mixer.music.play()
event.wait()