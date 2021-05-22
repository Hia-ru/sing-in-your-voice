from read_write_audio import *
from edit import block
import os
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
