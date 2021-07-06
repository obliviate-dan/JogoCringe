#!/usr/bin/python3

from os import path
from pydub import AudioSegment

# files                                                                         
src = "acabou.mp3"
dst = "acabou.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
