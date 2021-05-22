from read_write_audio import read_audio, write_audio
from edit import block
import os
from pathlib import Path

def search_mp3():
    p = Path("../")
    q = p/"res"
    mp3_list = list(q.glob('**/*.mp3'))
    return mp3_list

# [PosixPath('../res/1.mp3'), PosixPath('../res/3.mp3'), PosixPath('../res/2.mp3')]

while True:
    mp3_list = search_mp3()
    print('---- MP3 List ----')
    for mp3 in mp3_list:
        print(mp3)
    song = input('input your song file: ')
    name = song.rstrip('.mp3')
    song, sr = read_audio(name+'.mp3')
    origin = input('input original song file: ')
    origin, sr = read_audio(origin)
    ##
    #보컬추출 코드
    ##
    song = block(song, sr)
    song = song.match(origin)
    write_audio(song,name+'(수정됨).mp3')

#### code test ####

# from read_write_audio import write_audio

# audio_path = './test.mp3'
# yy , sr = lr.load(audio_path)

# audio_path = './2.mp3'
# sig , sr = lr.load(audio_path)
# size = sr*5
# sig = sig[0:size]
# # y = lr.effects.time_stretch(sig, 0.7)

# B = block(yy,sr)
# y = B.match(sig)
# print(sig.shape)
# print(yy.shape)
# print(type(y))

# write_audio('./',y,file_name='ttt')


# y,sr=read_audio('res/3.mp3')
# print(y)
# print(sr)