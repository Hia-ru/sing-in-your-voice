from read_write_audio import *
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
from multiprocessing import freeze_support

def search_mp3():
    mp3_list = ['추출','25-21']
    return mp3_list

def main():
    while True:
        freeze_support()
        # exe가 있는 폴더의 mp3 리스트 출력
        mp3_list = search_mp3()
        print('---- MP3 List ----')
        for mp3 in mp3_list:
            print(mp3)

        # 원본음원 입력
        while True:
            origin = input('input original song file: ').rstrip('.mp3')
            if not origin in mp3_list:
                print('Please re-enter')
                continue
            break

        # 노래음원 입력
        while True:
            song = input('input your song file: ').rstrip('.mp3')
            if not song in mp3_list:
                print('Please re-enter')
                continue
            break
        name = song

        # 음원 로딩
        print('\nloading and extracting vocal...\n')
        song, sr = read_audio(song+'.mp3')
        origin, music, sr = separate_vocal(origin+'.mp3',sr)
        
        # 보정
        print('\ncalibrating audio...\n')
        song = block(song, sr)
        song = song.match(origin)

        if len(song) == len(music):
            for s, m in zip(song, music):
                s = s + m

        # 저장
        name = name+'(수정됨)'
        write_audio(song,name)
        print('All completed. saved as '+name)

if __name__ == '__main__':
    main()
