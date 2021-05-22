from read_write_audio import *
from edit import block
import os
from multiprocessing import freeze_support

def search_mp3():
    mp3_list = ['(수정됨)','25-21']
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

        # 음원 로딩
        print('loading and extracting vocal...')
        origin, sr = read_audio(origin+'.mp3')
        song, sr = read_vocal(song+'.mp3',sr)

        # 보정
        print('\ncalibrating audio...\n')
        song = block(song, sr)
        song = song.match(origin,do_print_blocks=True)

        # 저장
        name = song+'(수정됨).mp3'
        write_audio(song,name)
        print('All completed. saved as '+name)

if __name__ == '__main__':
    main()
